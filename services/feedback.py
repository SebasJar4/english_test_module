from collections import defaultdict

def errors_by_topic(results):
    errors = defaultdict(int)
    for r in results:
        if not r.is_correct:
            errors[r.question.topic] += 1
    return dict(errors)

