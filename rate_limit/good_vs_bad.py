import matplotlib.pyplot as plt
import pandas as pd

file = 'data.csv'

data = pd.read_csv(
  file,
  sep=",", 
  usecols=["Time", "Source", "bad_packet"]
)

# paketit sekunteihin
data["second"] = data["Time"].astype(int)

bad = data[data["bad_packet"] == 1]
good = data[data["bad_packet"] == 0]

# hyvät ja pahat sekunnissa
good_rate = good.groupby("second").size()
bad_rate  = bad.groupby("second").size()

# paketit lähteittäin
packets_per_source = data.groupby("Source").size()
top_sources = packets_per_source.sort_values(ascending=False).head(5)
print(top_sources)

# kuvaaja
plt.plot(good_rate.index, good_rate.values, label="Hyvät")
plt.plot(bad_rate.index, bad_rate.values, label="Pahat")

plt.title("Hyvät vs pahat paketit")
plt.xlabel("Sekunnit")
plt.ylabel("Paketteja sekunnissa")

plt.legend()
plt.grid(True)

plt.show()