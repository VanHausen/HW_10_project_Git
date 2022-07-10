import result as result
from flask import json
from pip._internal.resolution.resolvelib import candidates


def load_candidates_json() -> list[dict]: # загрузит данные из файла
    with open(candidates.json, 'r', encoding='utf-8') as file:
        result = json.load(file)
        return result


def candidates_format(candidates: list[dict]) -> str:
    '''Форматирование списка кандидатов'''
    candidates: list[dict] = load_candidates_json()
    result = "<pre>"

    for candidate in candidates:
        result += f"""
            {candidate['name']}\n
            {candidate['position']}\n
            {candidate['skills']}\n
        """
    result += "<pre>"
    return result


def get_all() -> list[dict]:
    return load_candidates_json()


def get_candidate_id(uid: int) -> dict:
    candidates = get_all()
    for candidate in candidates:
        if candidate['id'] == uid:
            return candidate
    return None


def get_candidate_skill(skill: str) -> list[dict]:
    candidates = get_all()
    result = []
    for candidate in candidates:
        if skill in candidate['skills'].lower().split(', '):
            result.append(candidate)
    return result