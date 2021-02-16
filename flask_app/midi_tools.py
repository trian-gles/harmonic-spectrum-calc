import math

letter_dict = {'C':0, 'D':2, 'E':4, 'F':5, 'G':7, 'A':9, 'B':11}
accidental_dict = {'𝄰':1.25, '♯':1, '𝄱':0.75, '𝄲':0.5, '𝄮':0.25, '𝄯':-0.25, '𝄳':-0.5, '𝄬':-0.75, '♭':-1, '𝄭':-1.25}
midi_to_name_dict = {0:'C', 2:'D', 4:'E', 5:'F', 7:'G', 9:'A', 11:'B'}
midi_to_name_acc_dict = {0:'', 0.25:'𝄮', 0.5:'𝄲', 0.75:'𝄱', 1:'♯', -0.25:'𝄯', -0.5:'𝄳', -0.75:'𝄬', -1:'♭'}

def format_pitch(letter, register, acc=None):
    if acc:
        return letter + acc + register
    else:
        return letter + register

def get_partials(fundamental, n_limit, coefficient=1, shift=0):
    partial_list = []
    for rank in range(0, n_limit + 1):
        partial_list.append(shift + (fundamental * rank ** coefficient))
    return partial_list

def fund_to_series_name(fundamental, n_limit, coefficient=1, shift=0):
    partial_list = get_partials(fundamental, n_limit, coefficient, shift)
    partial_list.pop(0)
    partial_name_list = [freq_to_name(partial) for partial in partial_list]
    return partial_name_list


def freq_to_midi(freq):
    return 12 * math.log(freq / 440, 2) + 69

def midi_to_freq(midi):
    return 440 * 2 ** ((midi - 69) / 12)

def round_midi(midi):
    return round(midi * 4) / 4

def name_to_midi(note):
    letter = note[0].upper()
    if len(note) == 3:
        accidental = note[1]
        register = int(note[2]) + 1
    else:
        accidental = None
        register = int(note[1]) + 1
    midi_value = letter_dict[letter] + register * 12
    if accidental:
        midi_value += accidental_dict[accidental]
    return midi_value

def midi_to_name(midi_code):
    note = midi_code % 12
    if note in midi_to_name_dict.keys():
        letter = midi_to_name_dict[note]
        accidental = ''
    else:
        for key in midi_to_name_dict.keys():
            if abs(note - key) <= 1:
                letter = midi_to_name_dict[key]
                accidental = midi_to_name_acc_dict[note - key]
    register = ((midi_code - note) / 12) - 1
    return f"{letter}{accidental}{str(int(register))}"

def print_partial_names(fund):
    partials_freq = get_partials(fund, 16)
    for rank in range(1, 17):
        freq = partials_freq[rank]
        midi = freq_to_midi(freq)
        name = midi_to_name(round_midi(midi))
        print(rank, name, freq, midi)

def name_to_freq(name):
    return midi_to_freq(name_to_midi(name))

def freq_to_name(freq):
    return midi_to_name(round_midi(freq_to_midi(freq)))

def name_to_partials_name(name, n_limit, coefficient=1, shift=0):
    freq = name_to_freq(name)
    partials = get_partials(freq, n_limit, coefficient, shift)
    partials_name = []
    for partial in partials:
        if partial != 0:
            partials_name.append(freq_to_name(partial))
    return partials_name

def name_to_partials_dicts(name, n_limit, coefficient=1, shift=0):
    freq = name_to_freq(name)
    partials = get_partials(freq, n_limit, coefficient, shift)
    partial_dicts = []
    i = 1
    for partial in partials:
        if partial != 0:
            new_part = {}
            new_part['n'] = i
            new_part['pitch'] = freq_to_name(partial)
            new_part['midi'] = freq_to_midi(partial)
            new_part['freq'] = partial
            partial_dicts.append(new_part)
            i += 1
    return partial_dicts


if __name__ == "__main__":
    print(name_to_partials_dicts("G♯1", 16))
