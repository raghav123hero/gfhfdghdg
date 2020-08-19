import plotly.figure_factory as ff
import pandas as pd
import csv
import plotly.graph_objects as go
import random
import statistics



rag = pd.read_csv("StudentsPerformance.csv")
data = rag["reading score"].tolist()


mean = sum(data) / len(data)
median = statistics.median(data)
mode = statistics.mode(data)
std_deviation = statistics.stdev(data)

firstStd, firstStdEnd = mean-std_deviation, mean+std_deviation
secondStdStart, secondStdEnd = mean-(2*std_deviation), mean+(2*std_deviation)
thridStdStart, thridstdEnd = mean-(3*std_deviation), mean+(3*std_deviation)

hi = ff.create_distplot([data], ["reading scores"], show_hist=False)
hi.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
hi.add_trace(go.Scatter(x=[firstStd, firstStd], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
hi.add_trace(go.Scatter(x=[firstStdEnd, firstStdEnd], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
hi.add_trace(go.Scatter(x=[secondStdStart, secondStdStart], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
hi.add_trace(go.Scatter(x=[secondStdEnd, secondStdEnd], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
hi.show()



list_of_data_within_1_std_deviation = [result for result in data if result > firstStd and result < firstStdEnd]
list_of_data_within_2_std_deviation = [result for result in data if result > secondStdStart and result < secondStdEnd]
list_of_data_within_3_std_deviation = [result for result in data if result > thridStdStart and result < thridstdEnd]
print("Mean of this data is {}".format(mean))
print("Median of this data is {}".format(median))
print("Mode of this data is {}".format(mode))
print("Standard deviation of this data is {}".format(std_deviation))
print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(data)))
print("{}% of data lies within 2 standard deviations".format(len(list_of_data_within_2_std_deviation)*100.0/len(data)))
print("{}% of data lies within 3 standard deviations".format(len(list_of_data_within_3_std_deviation)*100.0/len(data)))
