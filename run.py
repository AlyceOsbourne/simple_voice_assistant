from speech_processing import speech_mode, console_mode

if __name__ == '__main__':
    if input('Speech mode? (y/n) ') == 'y':
        speech_mode()
    else:
        console_mode()
