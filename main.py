import flask
from utils import load_candidates_json, candidates_format, get_candidate_id, get_candidate_skill

app = flask.Flask(__name__)

@app.route("/")
def page_main():
  """Главная страница"""
  candidates: list[dict] = load_candidates_json()
  result = "<pre>"

  for candidate in candidates:
    result += f'''
      {candidate['name']}\n
      {candidate['position']}\n
      {candidate['skills']}\n
    '''
  result += "<pre>"
  return result


@app.route("/candidate/<int:uid>")
def page_candidate(uid):
  """Поиск кандидата по id"""
  candidate: dict = get_candidate_id(uid)
  result = f'<img src="{candidate["picture"]}">'
  result += candidates_format([candidate])
  return result


@app.route("/skills/<skill>")
def page_skills(skill):
  """Поиск кандидата по навыку"""
  skill_lower = skill.lower()
  candidates: list[dict] = get_candidate_skill(skill_lower)
  result = candidates_format(candidates)
  return result

app.run()