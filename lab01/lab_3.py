"""
    Created by Ian Park for CS344 at Calvin University, Spring 2020.

    Referenced from: https://ai-su13.artifice.cc/gps.html

    This program illustrates the limitation of the G.P.S. when faced "bad ideas"
    there is no "back up" that reconsiders prior actions. The algorithm
    must "do" the action in order to think.

    In this particular scenario, the GPS will find a way to "jump off the cliff" initially.
    Once that is done, it has to figure out how to land safely.
"""
from paip import gps

# Formulate the problem states and actions.
problem = {

    'initial': ['on top of cliff', 'safe', 'clueless'],
    'goal': ['landed safely', 'off cliff'],
    'badGoal': ['off cliff', 'landed safely'],

    'actions': [
        {
            'action': 'jump off cliff',
            'preconds': [
                'on top of cliff'
            ],
            'add': [
                'off cliff',
                'imminent death'
            ],
            'delete': [
                'safe',
                'on top of cliff'
            ],
        },
        {
            'action': 'land safely',
            'preconds': [
                'have plan',
            ],
            'add': [
                'landed safely'
            ],
            'delete': [
                'falling'
            ]
        },
        {
            'action': 'plan safe landing',
            'preconds': [
                'on top of cliff'
            ],
            'add': [
                'have plan'
            ],
            'delete': [
                'clueless'
            ]
        }
    ]
}


if __name__ == '__main__':
    # Use GPS to solve the problem formulated above.
    actionSequence = gps.gps(
        problem['initial'],
        problem['goal'],
        problem['actions']
    )

    print("Manually reordered solution:")
    # Print the solution, if there is one.
    if actionSequence is not None:
        for action in actionSequence:
            print(action)
    else:
        print('plan failure...')

    actionSequence = gps.gps(
        problem['initial'],
        problem['badGoal'],
        problem['actions']
    )


    print("Bad solution:")
    # Print the solution, if there is one.

    if actionSequence is not None:
        for action in actionSequence:
            print(action)
    else:
        print('plan failure...')
