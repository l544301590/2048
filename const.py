
SCREEN_A = 400

M_PANEL_A = 400
M_PANEL_MARGIN = (SCREEN_A - M_PANEL_A) / 2
M_PANEL_COLOR = (158, 158, 158)

BLOCK_A = 90
BLOCK_PROP = [  # ((bg color), (font color), font_size, (font_pos))
    ((84, 84, 84), (0, 0, 0), 50, (0, 0)),  # empty block
    ((101, 200, 147), (0, 0, 0), 50, (0, 0)),  # '2'
    ((101, 200, 180), (0, 0, 0), 50, (0, 0)),  # '4'
    ((101, 200, 147), (0, 0, 0), 50, (0, 0)),  # '8'
    ((101, 200, 147), (0, 0, 0), 50, (0, 0)),  # '16'
    ((101, 200, 147), (0, 0, 0), 50, (0, 0)),  # '32'
    ((101, 200, 147), (0, 0, 0), 50, (0, 0)),  # '64'
    ((101, 200, 147), (0, 0, 0), 50, (0, 0)),  # '128'
    ((101, 200, 147), (0, 0, 0), 50, (0, 0)),  # '256'
    ((101, 200, 147), (0, 0, 0), 50, (0, 0)),  # '512'
    ((101, 200, 147), (0, 0, 0), 50, (0, 0)),  # '1024'
    ((101, 200, 147), (0, 0, 0), 50, (0, 0))  # '2048'
]
BLOCK_MARGIN = (M_PANEL_A - 4*BLOCK_A) / 5

BLOCK_REGIONS = [
    [  # 1st row
        ((BLOCK_MARGIN*1+BLOCK_A*0, BLOCK_MARGIN*1+BLOCK_A*0), (BLOCK_A, BLOCK_A)),
        ((BLOCK_MARGIN*2+BLOCK_A*1, BLOCK_MARGIN*1+BLOCK_A*0), (BLOCK_A, BLOCK_A)),
        ((BLOCK_MARGIN*3+BLOCK_A*2, BLOCK_MARGIN*1+BLOCK_A*0), (BLOCK_A, BLOCK_A)),
        ((BLOCK_MARGIN*4+BLOCK_A*3, BLOCK_MARGIN*1+BLOCK_A*0), (BLOCK_A, BLOCK_A))
    ],
    [  # 2nd row
        ((BLOCK_MARGIN*1+BLOCK_A*0, BLOCK_MARGIN*2+BLOCK_A*1), (BLOCK_A, BLOCK_A)),
        ((BLOCK_MARGIN*2+BLOCK_A*1, BLOCK_MARGIN*2+BLOCK_A*1), (BLOCK_A, BLOCK_A)),
        ((BLOCK_MARGIN*3+BLOCK_A*2, BLOCK_MARGIN*2+BLOCK_A*1), (BLOCK_A, BLOCK_A)),
        ((BLOCK_MARGIN*4+BLOCK_A*3, BLOCK_MARGIN*2+BLOCK_A*1), (BLOCK_A, BLOCK_A))
    ],
    [  # 3rd row
        ((BLOCK_MARGIN*1+BLOCK_A*0, BLOCK_MARGIN*3+BLOCK_A*2), (BLOCK_A, BLOCK_A)),
        ((BLOCK_MARGIN*2+BLOCK_A*1, BLOCK_MARGIN*3+BLOCK_A*2), (BLOCK_A, BLOCK_A)),
        ((BLOCK_MARGIN*3+BLOCK_A*2, BLOCK_MARGIN*3+BLOCK_A*2), (BLOCK_A, BLOCK_A)),
        ((BLOCK_MARGIN*4+BLOCK_A*3, BLOCK_MARGIN*3+BLOCK_A*2), (BLOCK_A, BLOCK_A))
    ],
    [  # 4th row
        ((BLOCK_MARGIN*1+BLOCK_A*0, BLOCK_MARGIN*4+BLOCK_A*3), (BLOCK_A, BLOCK_A)),
        ((BLOCK_MARGIN*2+BLOCK_A*1, BLOCK_MARGIN*4+BLOCK_A*3), (BLOCK_A, BLOCK_A)),
        ((BLOCK_MARGIN*3+BLOCK_A*2, BLOCK_MARGIN*4+BLOCK_A*3), (BLOCK_A, BLOCK_A)),
        ((BLOCK_MARGIN*4+BLOCK_A*3, BLOCK_MARGIN*4+BLOCK_A*3), (BLOCK_A, BLOCK_A))
    ]
]  # relative to main_panel

# ui status
STATUS_MONITORING = 0
STATUS_ANIMATING = 1