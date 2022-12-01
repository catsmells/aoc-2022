elfcal <- function(.file, n = 1) {
  😃😃😃 <- as.integer(readLines(.file))
  😃😃😃[is.na(😃😃😃)] <- 0
  😃 <- cumsum(calories)
  😃😃 <- diff(😃[duplicated(😃)])
  if (n == 1) return(max(😃😃))
  sort(😃😃, decreasing = TRUE)[seq_len(n)] |>
    sum()
}
elfcal("input.dat")
elfcal("input.dat", 3)
