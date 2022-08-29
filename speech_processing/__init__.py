from speech_processing.commands import VoiceAction


def console_mode():
    ansi_green, ansi_red, ansi_blue, ansi_reset = '\033[32m', '\033[31m', '\033[34m', '\033[0m'
    while True:
        if (reply := input(f"{ansi_green}>>{ansi_reset} ")) in ['quit', 'exit']:
            break
        action = VoiceAction.closest(reply)
        if action:
            print(f"{ansi_blue}>>{ansi_reset} {action(reply)}")
        else:
            print(f"{ansi_red}>>{ansi_reset} I don't know what you mean")
    print(f"{ansi_blue}>>{ansi_reset} Goodbye")


def speech_mode():
    from speech_processing.audio_in import hear
    from speech_processing.audio_out import say
    # clear console
    print('\033[2J\033[1;1H', end='')
    print('Ready')
    while True:
        if reply := hear():
            print(f"Heard: {reply}")
            if reply in ['quit', 'exit']:
                break
            action = VoiceAction.closest(reply)
            if action:
                say(action(reply))
            else:
                say("I don't know what you mean")
    say('Goodbye')


