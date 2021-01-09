
# search4dwango9

## Doomworld discussions

 - https://www.doomworld.com/forum/topic/117097-whatever-happened-to-dwango9wad/
 - https://www.doomworld.com/forum/topic/119071-downloading-mirrors-of-idgames-tspg-and-wad-archive/

## Abstract

My attempt to help solving the DWANGO9 wad mystery.

Inspired by doomkid's idea in timestamp 3:08 of his video, I started working on a automated process to search for the dwango9 image in a WAD. As a Python programmer, I began my process by looking for a library to help me dump LUMP info more easily and I found Omgifol, originaly created by Fredrik Johansson and now maintened by Devin Acker (GitHub repo). First, I stored the data from the WOLF6 LUMP of the DWANGO!.WAD as our flag to be found. The rest of the algorithm is explained as follows:

 1. open a WAD loop through the possible groups of LUMPs in which the flag could be found (patches, flats, graphics, data)
 2. for each LUMP, compare its raw data with our flag's raw data
 3. if it matches, save in a text file the information where it was found to future inspection (WAD filename, LUMP name)
 4. repeat until the end of the WAD

Now it’s just a matter of running the script in batch for a large group of archived WADs and wait for something to come out. I've already started working on a different approach using computer vision to search for similar images so we don't rely on exact comparisons of raw LUMP data.

## Install package dependencies

```python
pip3 install --user omgifol
```

## Using the script

```python
python3 wadparser.py <wadfile> <dumpfile>
```

Example:

```python
python3 wadparser.py doom2.wad findings.txt
```

In the example above, all findings will be stored in the `findings.txt` file (opened in append mode).

