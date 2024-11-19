import pygame

screen = pygame.display.set_mode((950, 555))



skins = {

    'man': (
        [
            pygame.image.load('img/skins/man/right/Man_walk_1.png').convert_alpha(),
            pygame.image.load('img/skins/man/right/Man_walk_2.png').convert_alpha(),
            pygame.image.load('img/skins/man/right/Man_walk_3.png').convert_alpha(),
            pygame.image.load('img/skins/man/right/Man_walk_4.png').convert_alpha(),
            pygame.image.load('img/skins/man/right/Man_walk_5.png').convert_alpha(),
            pygame.image.load('img/skins/man/right/Man_walk_6.png').convert_alpha(),
        ],
        [
            pygame.image.load('img/skins/man/left/Man_Walk_1_reverse.png').convert_alpha(),
            pygame.image.load('img/skins/man/left/Man_Walk_2_reverse.png').convert_alpha(),
            pygame.image.load('img/skins/man/left/Man_Walk_3_reverse.png').convert_alpha(),
            pygame.image.load('img/skins/man/left/Man_Walk_4_reverse.png').convert_alpha(),
            pygame.image.load('img/skins/man/left/Man_Walk_5_reverse.png').convert_alpha(),
            pygame.image.load('img/skins/man/left/Man_Walk_6_reverse.png').convert_alpha(),
        ],
        [
            pygame.image.load('img/skins/man/death/Man_death_1.png').convert_alpha(),
            pygame.image.load('img/skins/man/death/Man_death_2.png').convert_alpha(),
            pygame.image.load('img/skins/man/death/Man_death_3.png').convert_alpha(),
            pygame.image.load('img/skins/man/death/Man_death_4.png').convert_alpha(),
        ]
    ),
    
    'woman': (
        [
            pygame.image.load('img/skins/women/right/1.png').convert_alpha(),
            pygame.image.load('img/skins/women/right/2.png').convert_alpha(),
            pygame.image.load('img/skins/women/right/3.png').convert_alpha(),
            pygame.image.load('img/skins/women/right/4.png').convert_alpha(),
            pygame.image.load('img/skins/women/right/5.png').convert_alpha(),
            pygame.image.load('img/skins/women/right/6.png').convert_alpha(),
        ],
        [
            pygame.image.load('img/skins/women/left/1.png').convert_alpha(),
            pygame.image.load('img/skins/women/left/2.png').convert_alpha(),
            pygame.image.load('img/skins/women/left/3.png').convert_alpha(),
            pygame.image.load('img/skins/women/left/4.png').convert_alpha(),
            pygame.image.load('img/skins/women/left/5.png').convert_alpha(),
            pygame.image.load('img/skins/women/left/6.png').convert_alpha(),
        ],
        [
            pygame.image.load('img/skins/women/death/1.png').convert_alpha(),
            pygame.image.load('img/skins/women/death/1.png').convert_alpha(),
            pygame.image.load('img/skins/women/death/1.png').convert_alpha(),
            pygame.image.load('img/skins/women/death/1.png').convert_alpha(),
        ]
    ),
    'girl': (
        [
            pygame.image.load('img/skins/girl/right/1.png').convert_alpha(),
            pygame.image.load('img/skins/girl/right/2.png').convert_alpha(),
            pygame.image.load('img/skins/girl/right/3.png').convert_alpha(),
            pygame.image.load('img/skins/girl/right/4.png').convert_alpha(),
            pygame.image.load('img/skins/girl/right/5.png').convert_alpha(),
            pygame.image.load('img/skins/girl/right/6.png').convert_alpha(),
        ],
        [
            pygame.image.load('img/skins/girl/left/1.png').convert_alpha(),
            pygame.image.load('img/skins/girl/left/2.png').convert_alpha(),
            pygame.image.load('img/skins/girl/left/3.png').convert_alpha(),
            pygame.image.load('img/skins/girl/left/4.png').convert_alpha(),
            pygame.image.load('img/skins/girl/left/5.png').convert_alpha(),
            pygame.image.load('img/skins/girl/left/6.png').convert_alpha(),
        ],
        [
            pygame.image.load('img/skins/girl/death/1.png').convert_alpha(),
            pygame.image.load('img/skins/girl/death/2.png').convert_alpha(),
            pygame.image.load('img/skins/girl/death/3.png').convert_alpha(),
            pygame.image.load('img/skins/girl/death/4.png').convert_alpha(),
        ]
    ),
    'boy': (
        [
            pygame.image.load('img/skins/boy/right/1.png').convert_alpha(),
            pygame.image.load('img/skins/boy/right/2.png').convert_alpha(),
            pygame.image.load('img/skins/boy/right/3.png').convert_alpha(),
            pygame.image.load('img/skins/boy/right/4.png').convert_alpha(),
            pygame.image.load('img/skins/boy/right/5.png').convert_alpha(),
            pygame.image.load('img/skins/boy/right/6.png').convert_alpha(),
        ],
        [
            pygame.image.load('img/skins/boy/left/1.png').convert_alpha(),
            pygame.image.load('img/skins/boy/left/2.png').convert_alpha(),
            pygame.image.load('img/skins/boy/left/3.png').convert_alpha(),
            pygame.image.load('img/skins/boy/left/4.png').convert_alpha(),
            pygame.image.load('img/skins/boy/left/5.png').convert_alpha(),
            pygame.image.load('img/skins/boy/left/6.png').convert_alpha(),
        ],
        [
            pygame.image.load('img/skins/boy/death/1.png').convert_alpha(),
            pygame.image.load('img/skins/boy/death/2.png').convert_alpha(),
            pygame.image.load('img/skins/boy/death/3.png').convert_alpha(),
            pygame.image.load('img/skins/boy/death/4.png').convert_alpha(),
        ]
    )


}
