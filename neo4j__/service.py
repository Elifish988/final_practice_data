import json
import csv

class Repository:
    def __init__(self, driver):
        self.driver = driver

    def load_data_to_neo4j(self):
        # Load CSV data into Neo4j
        with open(r"C:\Users\Eli Fishman\PycharmProjects\proj_data\students-profiles.csv", 'r') as csvfile:
            csvreader = csv.DictReader(csvfile)
            with self.driver.session() as session:
                for row in csvreader:
                    session.run("""
                    CREATE (:Person {
                        id: toInteger($id),
                        first_name: $first_name,
                        last_name: $last_name,
                        age: toInteger($age),
                        address: $address
                    });
                    """,
                    id=row["id"],
                    first_name=row["first_name"],
                    last_name=row["last_name"],
                    age=row["age"],
                    address=row["address"])

        # Load JSON data into Neo4j
        with open(r"C:\Users\Eli Fishman\PycharmProjects\proj_data\academic_network.json", 'r') as file:
            json_data = json.load(file)

        with self.driver.session() as session:
            # Create Teacher nodes from JSON
            for teacher in json_data["teachers"]:
                session.run("""
                CREATE (:Teacher {
                    id: $id,
                    name: $name,
                    department: $department,
                    title: $title,
                    office: $office,
                    email: $email
                });
                """,
                id=teacher["id"],
                name=teacher["name"],
                department=teacher["department"],
                title=teacher["title"],
                office=teacher["office"],
                email=teacher["email"])

            # Create Class nodes and relationships with Teacher
            for cls in json_data["classes"]:
                session.run("""
                CREATE (c:Class {
                    id: $id,
                    course_name: $course_name,
                    section: $section,
                    department: $department,
                    semester: $semester,
                    room: $room,
                    schedule: $schedule
                })
                WITH c
                MATCH (t:Teacher {id: $teacher_id})
                CREATE (t)-[:TEACHES]->(c);
                """,
                id=cls["id"],
                course_name=cls["course_name"],
                section=cls["section"],
                department=cls["department"],
                semester=cls["semester"],
                room=cls["room"],
                schedule=cls["schedule"],
                teacher_id=cls["teacher_id"])

            # Create relationships between Person and Class based on the enrollments data
            enrollments = json_data.get("enrollments", [])  # Ensure the key exists
            for enrollment in enrollments:
                session.run("""
                MATCH (p:Person {id: $student_id}), (c:Class {id: $class_id})
                CREATE (p)-[:ENROLLED_IN {enrollment_date: $enrollment_date, relationship_type: $relationship_type}]->(c);
                """,
                student_id=enrollment["student_id"],
                class_id=enrollment["class_id"],
                enrollment_date=enrollment["enrollment_date"],
                relationship_type=enrollment["relationship_type"])
