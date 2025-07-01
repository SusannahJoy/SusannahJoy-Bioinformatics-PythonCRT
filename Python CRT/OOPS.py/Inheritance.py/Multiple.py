class SportsCoach:
    def __init__(self):
        super().__init__()
    def coach_info(self):
        print("Teaches Football")
class MusicInstructor:
    def __init__(self):
        super().__init__()
    def music_info(self):
        print("Teaches Guitar")
class MultiTalentTeacher(SportsCoach,MusicInstructor):
    def __init__(self):
        super().__init__()
    def display(self):
        print("Handles sports and music.")
S1=SportsCoach()
S1.coach_info()
H1=MultiTalentTeacher()
H1.display()