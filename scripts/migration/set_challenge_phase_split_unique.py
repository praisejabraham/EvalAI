# Command to run: python manage.py shell < scripts/migration/set_challenge_phase_split.py
# Related to #1356 (https://github.com/Cloud-CV/EvalAI/pull/1356/)

from challenges.models import ChallengePhaseSplit


def set_challenge_phase_split_unique():

    challenge_phase_splits = ChallengePhaseSplit.objects.all().order_by('-pk')
    for challenge_phase_split in challenge_phase_splits:
        if ChallengePhaseSplit.objects.filter(dataset_split=challenge_phase_split.dataset_split,
            challenge_phase=challenge_phase_split.challenge_phase).count() > 1:
            challenge_phase_split.delete()

set_challenge_phase_split_unique()
