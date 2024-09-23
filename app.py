from pydantic import BaseModel
from typing import Dict, List, Tuple, Union

from fastapi import FastAPI
from unidecode import unidecode
import uvicorn

try:
    from cfuzzyset import cFuzzySet as FuzzySet
except ImportError:
    from fuzzyset import FuzzySet


app = FastAPI()


DATA = {
    "Python",
    "pythonista",
    "pythonic",
    "Python programming language",
    "Python 3.11",
    "Python 3.10",
    "Java language",
    "Java programming language",
    "Javascript",
    "OOD (Object-oriented programming)",
    "CI/CD",
    "Continuous Integration",
    "Continuous Deployment",
    "BASH",
    "Unix shell scripting",
}

JSON_EXAMPLE = """{"query": "py"}"""



DATABASE = FuzzySet(use_levenshtein=True, rel_sim_cutoff=0.1)
for term in DATA:
    DATABASE.add(unidecode(term.lower()))



class PartialSearchTerm(BaseModel):
	prefix: str


def get_app_description():
	return (
    	"Autocomplete endpoint example.\n\n"
    	"This API returns a list of words matching a given sequence of input characters. "
    	"Use the '/get_completions/' endpoint with a POST request to make predictions. "
    	f"Example usage: POST to '/get_completions/' with JSON data formatted as shown here:\n\n{JSON_EXAMPLE}"
	)


def _get_completions(substring: str) -> List[Tuple[float, str]]:
    candidates = DATABASE.get(substring)
    return [
        {
            "similarity": round(score, 2),
            "text": candidate
        } for score, candidate in candidates
    ]


@app.get("/")
async def root() -> Dict[str, str]:
	return {'message': get_app_description()}


@app.post("/predict/")
async def get_completions(
    partial_search_term: PartialSearchTerm
) -> List[Dict[str, Union[str, float]]]:
	completions = _get_completions(partial_search_term.prefix)
	return completions



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
