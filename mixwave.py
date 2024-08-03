import numpy as np
import wave

def generate_wave(frequency, duration, sample_rate=44100):
    """Gera uma onda senoidal com uma frequência e duração específicas."""
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave_data = np.sin(2 * np.pi * frequency * t)
    return wave_data

def mix_waves(wave1, wave2):
    """Mistura duas ondas somando seus valores."""
    return wave1 + wave2

def save_wave_file(filename, audio_data, sample_rate=44100):
    """Salva os dados de áudio em um arquivo WAV."""
    # Normalizar o áudio para o intervalo [-1, 1]
    audio_data = audio_data / np.max(np.abs(audio_data))
    audio_data = (audio_data * 32767).astype(np.int16)
    
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)  # Mono
        wf.setsampwidth(2)  # 16-bit
        wf.setframerate(sample_rate)
        wf.writeframes(audio_data.tobytes())

def main():
    # Solicita os dados ao usuário
    freq1 = float(input("Digite a primeira frequência (Hz): "))
    freq2 = float(input("Digite a segunda frequência (Hz): "))
    duration = float(input("Digite a duração em segundos: "))

    # Gera as duas ondas senoidais
    wave1 = generate_wave(freq1, duration)
    wave2 = generate_wave(freq2, duration)

    # Mistura as duas ondas
    mixed_wave = mix_waves(wave1, wave2)

    # Salva o áudio em um arquivo WAV
    output_filename = "mixed_output.wav"
    save_wave_file(output_filename, mixed_wave)

    print(f"Áudio salvo em {output_filename}")
print("\x1bc\x1b[47;34m")
if __name__ == "__main__":
    main()

