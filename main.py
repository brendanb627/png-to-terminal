import png_to_rgb_converter
from rgb_to_ansi import rgb_to_ansi256

sample_rate = 1

length = 60
width = 45
rgb_data = png_to_rgb_converter.png_to_rgb("image.png")
sample_count = 0
final_samples = []
for i in range(0, len(rgb_data) - (length * (sample_rate - 1)), sample_rate):
    samples = []
    for j in range(sample_rate):
        # final_samples.append(rgb_data[(i) + (j * length):((i + sample_rate)) + (j * length)])
        final_samples.append(rgb_data[(i) + (j * length)])

    # avg_c = [0, 0, 0]
    # for sample in samples:
    #     pass
        
    #     avg_c[0] += int(sample[0][0])
    #     avg_c[1] += int(sample[0][1])
    #     avg_c[2] += int(sample[0][2])
    # for n in range(len(avg_c)):
    #     avg_c[n] /= len(samples)
    # sample_count += 1
    # final_samples.append(avg_c)

for w in range(width):
    line = ""
    for l in range(length):
        index = (w * length) + l
        r, g, b = final_samples[index]
        line += f"\033[38;2;{int(r)};{int(g)};{int(b)}m██"
    print(line)
        
# ██