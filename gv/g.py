from module.classes import conf_class, midi_class, state_class

MY_CONF = conf_class.ConfClass()
MY_MIDI = midi_class.MidiClass()
MY_STATE = state_class.StateClass()

def reset_class():
    MY_CONF.__init__()
    MY_MIDI.__init__()
    MY_STATE.__init__()