import requests
from flask import Flask
from pip._internal.resolution.resolvelib import candidates
from utils import load_candidates_json, candidates_format, get_candidate_id, get_candidate_skill

app = Flask(__name__)

@app.route("/")
def page_main():
  '''Главная страница'''
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
  '''Поиск кандидата по id'''
  candidate: dict = get_candidate_id(uid)
  result = f'<img src="{candidate["picture"]}">'
  result += candidates_format([candidate])
  return result


@app.route("/skills/<skill>")
def page_skills(skill):
  '''Поиск кандидата по навыку'''
  skill_lower = skill.lower()
  candidate: list[dict] = get_candidate_skill(skill_lower)
  result = candidates_format(candidates)
  return result

app.run(host='0.0.0.0', port=8000)