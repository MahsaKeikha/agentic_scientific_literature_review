from run import run

def test_smoke(): assert run({})["system"] == "F90" and run({})["human_review_required"]
