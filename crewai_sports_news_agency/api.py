from flask import Flask, request, jsonify
from utilities.postgresql_utils import PostgresDB

app = Flask(__name__)

def get_game_score(team_name):
    db = PostgresDB(user="samisabir-idrissi", password="localmacm1", host="127.0.0.1", port="5433", database="template1")
    conn = db.connect()
    c = conn.cursor()
    print(team_name)
    c.execute("SELECT * from games WHERE team_name = %s;", (team_name,))
    result = c.fetchone()
    print(f'results: {result}')
    db.get_column_names(conn,"games")
    if result:
        keys = ["team_name", "game_id", "status", "home_team", "home_team_score", "away_team","away_team_score"]
        # game_score = dict(zip(keys, result))
        # print(f'game score: {game_score}')
        return dict(zip(keys, result))
    else:
        return {'error': 'No game scores found for the team.'}
    


@app.route('/')
def home():
    return jsonify({
        'message': 'Welcome to the NBA Scores API. Use /score?team=<team_name> to fetch game scores.'
    })

@app.route('/score', methods=['GET'])
def score():
    team_name = request.args.get('team', '')
    if not team_name:
        return jsonify({'error': 'Missing team name'}), 400
    score = get_game_score(team_name)
    return jsonify(score)

if __name__ == '__main__':
    app.run(debug=True)