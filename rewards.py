

class Rewards:

    @staticmethod
    def show_all():
        return 'select * from rewards;', []

    @staticmethod
    def select():
        place = input('Enter place:')
        team_name = input('Enter team name:')
        sport_name = input('Enter sport name:')
        competition_name = input('Enter competition name:')
        competition_date = input('Enter competition date:')
        return "select * from rewards where place = %s and team_name = %s " \
               "and sport_name = %s and competition_name = %s " \
               "and competition_date = %s", [place, team_name, sport_name, competition_name, competition_date]

    @staticmethod
    def delete():
        place = input('Enter place:')
        team_name = input('Enter team name:')
        sport_name = input('Enter sport name:')
        competition_name = input('Enter competition name:')
        competition_date = input('Enter competition date:')
        return "delete from rewards where place = %s and team_name = %s " \
               "and sport_name = %s and competition_name = %s " \
               "and competition_date = %s;", [place, team_name, sport_name, competition_name, competition_date]

    @staticmethod
    def insert():
        place = input('Enter place:')
        prize = input('Enter prize:')
        team_name = input('Enter team name:')
        sport_name = input('Enter sport name:')
        competition_date = input('Enter competition date:')
        competition_name = input('Enter competition name:')
        return "insert into rewards (place, prize, team_name," \
               "sport_name, competition_date, competition_name) VALUES (%s, %s, %s, %s, %s, %s)", \
               [place, prize, team_name, sport_name, competition_date, competition_name]

    @staticmethod
    def update():
        place = input('Enter place:')
        prize = input('Enter prize:')
        team_name = input('Enter team name:')
        sport_name = input('Enter sport name:')
        competition_date = input('Enter competition date:')
        competition_name = input('Enter competition name:')
        return "update rewards set prize = %s " \
               "where place = %s and team_name = %s and sport_name = %s and competition_date = %s " \
               "and competition_name = %s", [prize, place, team_name, sport_name, competition_date, competition_name]