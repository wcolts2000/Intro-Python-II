from sys import stdout, exit
from os import system


def outside():
    print('OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO')
    print('OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO')
    print('OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOoOOooooooOoOOoOOOOO')
    print('OOOOOOOOOOOOOOOOOOOOOOOOOOOoooo/[[/**`/ooooooOOOO')
    print('OOOOOoOOOOOOOOOOOOOOOOOOOOoo`*.      ..**,/oOOOOO')
    print('O/OO^=[OOOOOOOOOOOOOOOo//o/`.           .**ooOOOO')
    print('O///O=*=OOOOOOOOOOOOO^/O/ ..             .,,OooOO')
    print('O/O/O/,OOOOOOOOOOOO[O=Oo` .              .]/oOOOO')
    print('/.O`=.=OOOOOOOOOOOO^O=OO/`,.          .,.=o^OOOOO')
    print('//O/O/=OOOOOOOOOOOO//.O//`/. ./o`  ./=o/OOO[/OOO/')
    print('`OO,O.O.O/,/OOOOOO\O\]//o[/  ...`..``/=`,/OO[^,O/')
    print('O/O/`///,/` /]`        ,[[ =`.   ` /, `,.,//O/OOO')
    print('/,O//OOOO],[.]`                    .///`OOOOOOOOO')
    print('/OOOOOOOOOO][=/[.             `]O/OOOOOOOOOOOOOOO')
    print('/OOOOOOOOO//OO]/O/` ,``]^/OOOOOOOOOOOOOOOOOOOOOOO')
    print('OOOOOOOOOOOOOOOOO/=OOOO/OO^/OOOOOOOOOOOOOOOOOOOOO' + '\n')


def foyer():
    print('###################             #################')
    print('###################             #################')
    print('##                                             ##')
    print('##                                             ##')
    print('##                                             ##')
    print('##                                               ')
    print('##                                               ')
    print('##                                               ')
    print('##                                             ##')
    print('##                                             ##')
    print('##                                             ##')
    print('##                                             ##')
    print('##                                             ##')
    print('##                                             ##')
    print('###################             #################')
    print('###################             #################' + '\n')


def overlook():
    print('#################################################')
    print('#################################################')
    print('#################################################')
    print('#################################################')
    print('#################################################')
    print('#################################################')
    print('#################################################')
    print('#################################################')
    print('##                                             ##')
    print('##                                             ##')
    print('##                                             ##')
    print('##                                             ##')
    print('##                                             ##')
    print('##                                             ##')
    print('###################             #################')
    print('###################             #################' + '\n')


def narrow():
    print('######################     ######################')
    print('######################     ######################')
    print('######################     ######################')
    print('######################      #####################')
    print('######################       ####################')
    print('   ####################        ##################')
    print('    ####################       ##################')
    print('      ####################        ###############')
    print('#              #######          #################')
    print('###                           ###################')
    print('##########                #######################')
    print('##############         ##########################')
    print('#################################################')
    print('#################################################')
    print('#################################################')
    print('#################################################' + '\n')


def treasure():
    print('#################################################')
    print('#################################################')
    print('#################################################')
    print('#################################################')
    print('########                                 ########')
    print('########                                 ########')
    print('########                      /          ########')
    print('########                  |__|           ########')
    print('########                                 ########')
    print('########                                 ########')
    print('########                                 ########')
    print('########                                 ########')
    print('########                                 ########')
    print('########                                 ########')
    print('######################     ######################')
    print('######################     ######################' + '\n')


def grave(player_name, player_items):
    print('ooooooooooooooooooooooooooooooooooooooooooooooooo')
    print('ooooooooooooooooooooooooooooooooooooooooooooooooo')
    print('ooooooooooooooooooooooooooooooooooooooooooooooooo')
    print('ooooooooooooooooooooooooooooooooooooooooooooooooo')
    print('oooooooooooooooooooooo[    [ooooooooooooooooooooo')
    print('oooooooooooooooooo/`           /Ooooooooooooooooo')
    print('ooooooooooooooooO     R.I.P.     =ooooooooooooooo')
    print('ooooooooooooooooo                =ooooooooooooooo')
    print('ooooooooooooooooo   ,    .       =ooooooooooooooo')
    print('ooooooooooooooooo   =/[^ ^=/[O   =ooooooooooooooo')
    print('ooooooooooooooooo   =OO` ^=OO/   =ooooooooooooooo')
    print('ooooooooooooooooo   ,`,` `,`     =ooooooooooooooo')
    print('ooooooooooooooooo                =ooooooooooooooo')
    print('ooooooooooooooooo                =ooooooooooooooo')
    print('oooooooooooo/[[[[                ,[[[/ooooooooooo')
    print('oooooooooooo^ ]@@/]]]]     ,]]`      =/oooooooooo')
    print('oooooooooO@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@oooooo')
    print('ooooooo@@@@O@OOOOOOOOOOOOO/[[/OOOOOOOOOOOO@Oooooo')
    print('ooooo/`......................................=ooo')
    print('oooo/.........................................ooo')
    print('ooooooOO@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@OOoooo' + '\n')
    print(f'          --- Here lies {player_name} ---       \n')
    if len(player_items) > 0:
        print(f'They were found with: {player_items} \n')
    else:
        print(f'They were found with  nothing on them')


def cobra():
    print('    .,]@@@@@@/`                                  ')
    print('  /@]OOOOO@@/OOOO/`...               ...         ')
    print(' ,OOOOOOO///OOOOOOOOO/`            ....          ')
    print('@OO@OOOOOOO@@OO@@OOOO@OO/.        .              ')
    print(',O@@@@@@/O@^OO@///OOO/./`,/                      ')
    print('.` =^  @//@O@`=^..@=O@./*.*^                     ')
    print('    ,@//@O@/,[[/,`=^O@/....=.                    ')
    print(' ,]@...,`..,]]]@[]/^O@^,`..=^                    ')
    print(' ..   ,^...**],/`.//O@@.,`.=.                    ')
    print('    ..^......./`.=/OO@,^.,.@         ..          ')
    print('  . .=....*.//..=OOO@`.,..=^      ..             ')
    print('  ...^...[[@`.//OOO@/^..../        ...           ')
    print('    .^..,]/*=`@OOO@..^.../.                      ')
    print('    .^..,`=`/OOOO`=...../.                       ')
    print('     ^,/,`,@OOO/=.*..../               ,]]]]]]]]]')
    print('    .@``,@OOO//....../`             =@@/[.       ')
    print('   ,//./OOO``.`...,/`               ,@@@@@@@/].  ')
    print('   @`,@OO/....,]/`  ..                ..[[[[/@@@/')
    print('  =*,@OO/.,//`    .. .]@@@@@@@@@@@@@@@@@/]]]]/@@@')
    print(' .=/]@OO^/         ,@@@@@O@@@@@OOOOOOOOOOOOOOOOO@')
    print('  =`.@OO@.         @@@@/`           .[[[[[[[[`.  ')
    print('  .^[@OO@^         /@@@@].                       ')
    print('   ==@@OO@/        ./@@@@@@@@@@@/]]].            ')
    print('    /@@OOOO@]        .[/@@@@@@@@@@@@@OO@`        ')
    print('     /@@OOOOOO@`                  .[@@OOO`       ')
    print('   ...,@@@OOOOOOOO@/]..            ,@@OO@.       ')
    print('  ... . ./@@@@OOOOOOOOOOO@@@@@@@@@@OOOO@^        ')
    print('  ....      [@@@@@@OOOOOOOOOOOOOOOOOOO/.         ')
    print('                 .[[/@@@@@@@@@@@@@[[..    ' + '\n')


def dark():
    print('#################################################')
    print('#################################################')
    print('#################################################')
    print('#################################################')
    print('#################################################')
    print('#################################################')
    print('#################################################')
    print('#################################################')
    print('#################################################')
    print('#################################################')
    print('#################################################')
    print('#################################################')
    print('#################################################')
    print('#################################################')
    print('#################################################')
    print('#################################################')
    print('#################################################' + '\n')


#######################################
#  Terminal Output Helpers
#######################################


def title_screen_selections(setup_game):
    option = input('> ')
    if option.lower() in ['play', 'p']:
        system('clear')
        setup_game()
    elif option.lower() in ['help', 'h']:
        system('clear')
        help_menu(setup_game)
    elif option.lower() in ['quit', 'q']:
        system('clear')
        exit()
    while option.lower() not in ['play', 'p', 'help', 'h', 'quit', 'q']:
        system('clear')
        print("please enter a valid command.")
        title_screen_selections(setup_game)


def header():
    print('#################################################')
    print('#         Welcome to "Adventure Lurks"!         #')
    print('#################################################' + '\n')


def title_screen(setup_game):
    header()
    print('- Play - ')
    print('- Help - ')
    print('- Quit - ')
    title_screen_selections(setup_game)


def help_menu(setup_game):
    header()
    print('  - Type "play" or "p" to start the game -            ')
    print('  - Use "n", "s", "e", "w" to move -                  ')
    print('  - Use "examine" or "ex" to inspect surroundings -   ')
    print('  - Use "quit" or "q" to stop the game -              ')
    print('  - Type 2 commands to interact -                     ')
    print('  - Typing "take <item name>" will pick up an item  - ')
    print('  - Typing "drop <item name>" will drop an item  -    ')
    print('  - Good luck and have fun!!! -                       ')
    print('  - Play - Help - Quit -                              ')
    title_screen_selections(setup_game)


def generate_screen(room_name):
    if room_name == 'Outside The Cave Entrance':
        outside()
    elif room_name == 'Foyer':
        foyer()
    elif room_name == 'Grand Overlook':
        overlook()
    elif room_name == 'Narrow Passage':
        narrow()
    elif room_name == 'Treasure Chamber':
        treasure()
    elif room_name == 'Pitch Black':
        dark()
