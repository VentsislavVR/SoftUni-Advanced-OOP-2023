def gather_credits(needed_cred, *args):
    my_courses = {}
    success = False
    res = []
    gained_credits = 0
    for clas,credits in args:
        if clas not in my_courses and needed_cred > gained_credits:
            my_courses[clas] = int(credits)
            gained_credits += my_courses[clas]

            if gained_credits >=needed_cred:

                break


    if gained_credits >=needed_cred:
        res.append(f'Enrollment finished! Maximum credits: {gained_credits}.\nCourses:')
        for c in sorted(my_courses):
            res.append(f"{c},")

    else:
        res.append(f"You need to enroll in more courses! You have to gather {needed_cred-gained_credits} credits more.")

    return ' '.join(res).rstrip(',')

print(gather_credits(
    80,
    ("Basics", 27),
))
print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))
print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))








from unittest import TestCase, main


class Test(TestCase):
    def test_students_credits(self):
        result = gather_credits(
            60,
            ("Basics", 27),
            ("Fundamentals", 27),
            ("Advanced", 30),
            ("Web", 30)

        )

        self.assertEqual(
            result.strip(),
            """Enrollment finished! Maximum credits: 84.
Courses: Advanced, Basics, Fundamentals""")


if __name__ == '__main__':
    main()
from unittest import TestCase, main


class Test(TestCase):
    def test_students_credits(self):
        result = gather_credits(
            80,
            ("Advanced", 30),
            ("Basics", 27),
            ("Fundamentals", 27),

        )

        self.assertEqual(
            result.strip(),
            """Enrollment finished! Maximum credits: 84.
Courses: Advanced, Basics, Fundamentals""")


if __name__ == '__main__':
    main()