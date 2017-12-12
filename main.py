# coding=UTF-8

import csv
import operator
import sys

try:
    raw_data = dict()
    file_csv = open(sys.argv[1], 'r')
    reader = csv.reader(file_csv)
    print("\nProcessing %s\n" % sys.argv[1])
    for _, _, _, _, _, _, _, _, _, time, _, _, _, ms_interval , _ in reader:
        if time != 'TimeInSeconds' and float(ms_interval) != 0:
            raw_data[float(time)] = (1000/float(ms_interval), float(ms_interval))
    percent = int(raw_data.__len__()/100)
    sorted_data = sorted(raw_data.items(), key=operator.itemgetter(1))
    sorted_fps = [int(i[1][0]) for i in sorted_data]
    avg_delay = sum(ms for _, ms in raw_data.values())/raw_data.__len__()
    avg_fps = sum(fps for fps, _ in raw_data.values())/raw_data.__len__()
    highest_1 = sum(sorted_fps[0:percent])/percent
    highest_10th = sum(sorted_fps[0:(int(percent/10))])/(int(percent/10))
    print("Average delay : %.1f ms\n"
          "Average FPS : %.1f fps\n"
          "1%% lowest : %.1f fps\n"
          "0.1%% lowest : %.1f fps\n"
          % (avg_delay, avg_fps, highest_1, highest_10th))
    file_csv.close()

except IOError:
    print ("Impossible to open the file. Make sure you entered the "
           "correct path and that the file isn't used by another program")