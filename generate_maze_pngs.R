# check wd
getwd()

# create a dataframe for labels
x <- 0:4
y <- 0:4
df <- data.frame(matrix(ncol=2, nrow=1))
for (x_val in x) {
  for (y_val in y) {
    df <- rbind(df, c(x_val, y_val))
  }
}

# remove empty first row
df <- df[-1,]

# row and column titles
rownames(df) <- letters[1:nrow(df)]
names(df) <- c("x_value", "y_value")

# check plot and labels
plot(df)
text(df[,1] + 0.10, df[,2], labels=rownames(df), cex=0.7)

### GET DATA

# get the maze data for maze 1
maze_points <- read.table("maze_edges.txt")
edges <- read.table("maze_coordinate_pairs.txt")

# get data for maze 2
maze_points2 <- read.table("maze_edges2.txt")
edges2 <- read.table("maze_coordinate_pairs2.txt")

# get data for maze 3
maze_points3 <- read.table("maze_edges3.txt")
edges3 <- read.table("maze_coordinate_pairs3.txt")


### GENERATE THE MAZE PLOT IMAGES

# generate maze 1 png
png(file="aMAZEd_graph.png", width=600, height=600)

plot(0:6, 0:6, type = "n", bty="n", main="Maze 1", xlab="", ylab="") + points(maze_points, pch=19, col = "darkorchid") + segments(edges[,1], edges[,2], edges[,3], edges[,4], col = "lightskyblue", lty = par("lty"), xpd = FALSE) + points(maze_points[1,], pch=19, col = "green") + points(maze_points[nrow(maze_points),], pch=19, col ="red")
text(df[,1] + 0.12, df[,2], labels=rownames(df), cex=0.7)
legend(5, 5, legend=c("start", "end"), 
       fill = c("green","red"))

# save image
dev.off()

# generate maze 2 png
png(file="aMAZEd_graph2.png", width=600, height=600)

# plot details
plot(0:6, 0:6, type = "n", bty="n", main="Maze 2", xlab="", ylab="") + points(maze_points2, pch=19, col = "darkorchid") + segments(edges2[,1], edges2[,2], edges2[,3], edges2[,4], col = "lightskyblue", lty = par("lty"), xpd = FALSE) + points(maze_points2[1,], pch=19, col = "green") + points(maze_points2[nrow(maze_points2),], pch=19, col ="red")
text(df[,1] + 0.12, df[,2], labels=rownames(df), cex=0.7)
legend(5, 5, legend=c("start", "end"), 
       fill = c("green","red"))

# save image
dev.off()



# generate maze 3 png
png(file="aMAZEd_graph3.png", width=600, height=600)


# plot details
plot(0:6, 0:6, type = "n", bty="n", main="Maze 3", xlab="", ylab="") + points(maze_points3, pch=19, col = "darkorchid") + segments(edges3[,1], edges3[,2], edges3[,3], edges3[,4],                                                                                                                                   col = "lightskyblue", lty = par("lty"), xpd = FALSE) + points(maze_points3[1,], pch=19, col = "green") + points(maze_points3[nrow(maze_points3),], pch=19, col ="red") 

# add labels to each point
text(df[,1] + 0.10, df[,2], labels=rownames(df), cex=0.7)

# add legend
legend(5, 5, legend=c("start", "end"), 
       fill = c("green","red"))

# save image
dev.off()





