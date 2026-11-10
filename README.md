# Streaming KV-Cache Compression

Code and benchmarks for **Streaming KV-Cache Compression for Memory-Bounded Decoding**
(ICML 2026).

## Repository layout

```
src/
  kv_cache.py        # streaming compressor
  decoder.py         # memory-bounded decoding loop
eval/
  benchmark.py       # throughput and quality benchmarks
results/
  icml2026_main.csv
requirements.txt
```

The released implementation is complete and reproduces the main ICML results.

## Citation

```
@inproceedings{brown2026streaming,
  title={Streaming KV-Cache Compression for Memory-Bounded Decoding},
  author={Brown, Brenda A. and Raman, Priya},
  booktitle={ICML 2026},
  year={2026}
}
```
