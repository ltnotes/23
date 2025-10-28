🎯 1️⃣ Basic plotting functions in R
🟢 Simple scatter plot
x <- c(1, 2, 3, 4, 5)
y <- c(2, 4, 6, 8, 10)
plot(x, y, type="p", col="blue", main="Simple Scatter Plot", xlab="X values", ylab="Y values")


type="p" = points

You can use type="l" for line, or "b" for both line and points.

🟢 Line plot
plot(x, y, type="l", col="red", main="Line Plot", xlab="X", ylab="Y")

🟢 Bar plot
heights <- c(20, 35, 30, 40)
names <- c("A", "B", "C", "D")
barplot(heights, names.arg=names, col="lightblue", main="Bar Chart", xlab="Category", ylab="Value")

🟢 Horizontal bar plot
barplot(heights, names.arg=names, horiz=TRUE, col="orange", main="Horizontal Bar Chart")

🟢 Histogram

Used for numeric data distributions.

data <- c(2, 4, 4, 6, 7, 8, 9, 10, 10, 12)
hist(data, col="lightgreen", main="Histogram of Data", xlab="Values", ylab="Frequency")

🟢 Box plot

Used to show median, quartiles, and outliers.

data <- c(5, 7, 8, 9, 10, 15, 20)
boxplot(data, main="Boxplot Example", col="pink", ylab="Values")

🟢 Pie chart
slices <- c(10, 20, 30, 40)
labels <- c("A", "B", "C", "D")
pie(slices, labels=labels, col=rainbow(length(slices)), main="Pie Chart Example")

🎯 2️⃣ Multiple plots in one window
par(mfrow=c(2,2))  # 2 rows, 2 columns
plot(x, y)
barplot(heights)
hist(data)
boxplot(data)
par(mfrow=c(1,1))  # reset layout
