.PHONY: all clean

all: report.txt

raw.txt:
	echo "alpha beta gamma" > $@

count.txt: raw.txt
	tr ' ' '\n' < $< | wc -l > $@

report.txt: count.txt
	echo "words: $$(cat $<)" > $@

clean:
	rm -f raw.txt count.txt report.txt
