

class Athletes:

    @staticmethod
    def show_all():
        return 'select * from athletes;', []

    @staticmethod
    def select():
        name = input('Enter athlete name:')
        return "select * from athletes where name = %s;", [name]

    @staticmethod
    def delete():
        name = input('Enter athlete name:')
        return "delete from athletes where name = %s;", [name]

    @staticmethod
    def insert():
        name = input('Enter athlete name:')
        height = input('Enter athlete height:')
        weight = input('Enter athlete weight:')
        age = input('Enter athlete age:')
        sex = input('Enter athlete sex:')
        team_name = input('Enter athlete team name:')
        sport_name = input('Enter athlete sport name:')
        return "insert into athletes (name, height, weight, age, sex, team_name, sport_name) VALUES" \
               "(%s, %s, %s, %s, %s, %s, %s)", [name, height, weight, age, sex, team_name, sport_name]

    @staticmethod
    def update():
        name = input('Enter athlete name:')
        height = input('Enter athlete height:')
        weight = input('Enter athlete weight:')
        age = input('Enter athlete age:')
        sex = input('Enter athlete sex:')
        team_name = input('Enter athlete team name:')
        sport_name = input('Enter athlete sport name:')
        return "update athletes set height = %s, weight = %s, age = %s, sex = %s, team_name = %s, sport_name = %s " \
               "where name = %s;", [height, weight, age, sex, team_name, sport_name, name]
