"""
    This module implements the simple blocks world using PAIP GPS.

    Modified by Ian Park for CS344 at Calvin University, Spring 2020.
    Adds two different problems specified in Lab01.
    Also, slightly changed gps import after putting paip-python in my
    virtualenv's site-packages.
"""
from paip.gps import gps

# Formulate the problem states and actions.
problem = {

    'initial': ['space on a', 'a on b', 'b on c', 'c on table', 'space on table'],
    'goal': ['space on c', 'c on b', 'b on a', 'a on table', 'space on table'],

    'actions': [
        {
            'action': 'move a from b to c',
            'preconds': [
                'space on a',
                'space on c',
                'a on b'
            ],
            'add': [
                'a on c',
                'space on b'
            ],
            'delete': [
                'a on b',
                'space on c'
            ]
        },
        {
            'action': 'move a from table to b',
            'preconds': [
                'space on a',
                'space on b',
                'a on table'
            ],
            'add': [
                'a on b'
            ],
            'delete': [
                'a on table',
                'space on b'
            ]
        },
        {
            'action': 'move a from b to table',
            'preconds': [
                'space on a',
                'space on table',
                'a on b'
            ],
            'add': [
                'a on table',
                'space on b'
            ],
            'delete': [
                'a on b'
            ]
        },
        {
            'action': 'move a from c to b',
            'preconds': [
                'space on a',
                'space on b',
                'a on c'
            ],
            'add': [
                'a on b',
                'space on c'
            ],
            'delete': [
                'a on c',
                'space on b'
            ]
        },
        {
            'action': 'move a from table to c',
            'preconds': [
                'space on a',
                'space on c',
                'a on table'
            ],
            'add': [
                'a on c'
            ],
            'delete': [
                'a on table',
                'space on c'
            ]
        },
        {
            'action': 'move a from c to table',
            'preconds': [
                'space on a',
                'space on table',
                'a on c'
            ],
            'add': [
                'a on table',
                'space on c'
            ],
            'delete': [
                'a on c'
            ]
        },
        {
            'action': 'move b from a to c',
            'preconds': [
                'space on b',
                'space on c',
                'b on a'
            ],
            'add': [
                'b on c',
                'space on a'
            ],
            'delete': [
                'b on a',
                'space on c'
            ]
        },
        {
            'action': 'move b from table to a',
            'preconds': [
                'space on b',
                'space on a',
                'b on table'
            ],
            'add': [
                'b on a'
            ],
            'delete': [
                'b on table',
                'space on a'
            ]
        },
        {
            'action': 'move b from a to table',
            'preconds': [
                'space on b',
                'space on table',
                'b on a'
            ],
            'add': [
                'b on table',
                'space on a'
            ],
            'delete': [
                'b on a'
            ]
        },
        {
            'action': 'move b from c to a',
            'preconds': [
                'space on b',
                'space on a',
                'b on c'
            ],
            'add': [
                'b on a',
                'space on c'
            ],
            'delete': [
                'b on c',
                'space on a'
            ]
        },
        {
            'action': 'move b from table to c',
            'preconds': [
                'space on b',
                'space on c',
                'b on table'
            ],
            'add': [
                'b on c'
            ],
            'delete': [
                'b on table',
                'space on c'
            ]
        },
        {
            'action': 'move b from c to table',
            'preconds': [
                'space on b',
                'space on table',
                'b on c'
            ],
            'add': [
                'b on table',
                'space on c'
            ],
            'delete': [
                'b on c'
            ]
        },
        {
            'action': 'move c from a to b',
            'preconds': [
                'space on c',
                'space on b',
                'c on a'
            ],
            'add': [
                'c on b',
                'space on a'
            ],
            'delete': [
                'c on a',
                'space on b'
            ]
        },
        {
            'action': 'move c from table to a',
            'preconds': [
                'space on c',
                'space on a',
                'c on table'
            ],
            'add': [
                'c on a'
            ],
            'delete': [
                'c on table',
                'space on a'
            ]
        },
        {
            'action': 'move c from a to table',
            'preconds': [
                'space on c',
                'space on table',
                'c on a'
            ],
            'add': [
                'c on table',
                'space on a'
            ],
            'delete': [
                'c on a'
            ]
        },
        {
            'action': 'move c from b to a',
            'preconds': [
                'space on c',
                'space on a',
                'c on b'
            ],
            'add': [
                'c on a',
                'space on b'
            ],
            'delete': [
                'c on b',
                'space on a'
            ]
        },
        {
            'action': 'move c from table to b',
            'preconds': [
                'space on c',
                'space on b',
                'c on table'
            ],
            'add': [
                'c on b'
            ],
            'delete': [
                'c on table',
                'space on b'
            ]
        },
        {
            'action': 'move c from b to table',
            'preconds': [
                'space on c',
                'space on table',
                'c on b'
            ],
            'add': [
                'c on table',
                'space on b'
            ],
            'delete': [
                'c on b'
            ]
        }
    ]
}

problemA = {
    'initial': ['space on table', 'space on b', 'b on table', 'space on c', 'c on a', 'a on table'],
    'goal': ['space on b', 'b on table', 'space on a', 'a on table', 'space on c', 'c on table'],
    'actions': problem['actions']
}

problemB = {
    'initial': ['space on a', 'a on table', 'space on b', 'b on table', 'space on c', 'c on table'],
    'goal': ['c on table', 'b on c', 'a on b', 'space on a'],
    'actions': problem['actions']
}

if __name__ == '__main__':

    # import logging

    # logging.basicConfig(level=logging.DEBUG)

    # Use GPS to solve the problems formulated above.
    actionSequence = gps(
        problem['initial'],
        problem['goal'],
        problem['actions']
    )

    actionSequenceA = gps(
        problemA['initial'],
        problemA['goal'],
        problemA['actions']
    )

    actionSequenceB = gps(
        problemB['initial'],
        problemB['goal'],
        problemB['actions']
    )

    # Print the solutions, if there is one.
    if actionSequence is not None:
        print("Default Problem:")
        for action in actionSequence:
            print(action)
    else:
        print('Default plan failure...')

    if actionSequenceA is not None:
        print("Problem A:")
        for action in actionSequenceA:
            print(action)
    else:
        print('A plan failure...')

    if actionSequenceB is not None:
        print("Problem B:")
        for action in actionSequenceB:
            print(action)
    else:
        print('B plan failure...')
