#!/usr/bin/env python3

#***********************************************
# Vector repeats each line entered
#***********************************************

import anki_vector


def main():

    text = ''

    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial) as robot:
        
        while text != 'q':
            text = input('Vector says:  ')
            robot.say_text(text)


if __name__ == "__main__":
    main()