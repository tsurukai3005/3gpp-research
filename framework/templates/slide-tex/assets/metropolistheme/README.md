# assets/metropolistheme — Metropolis テーマのベンダ予約ディレクトリ

`/render-tex-slides` の標準動作は **TeX Live 同梱の `\usetheme{metropolis}`** を使う前提で、
本ディレクトリにファイルを置く必要はない。

ベンダしたい場合（自己完結性を強めたい・特定フォーク版を固定したい）の手順:

1. ML-Precoding-for-Cell-Free-MIMO の `presentation/source/` から以下を取得:
   - `beamerthememetropolis.dtx`
   - `beamercolorthememetropolis.dtx`
   - `beamercolorthememetropolis-highcontrast.dtx`
   - `beamerfontthememetropolis.dtx`
   - `beamerinnerthememetropolis.dtx`
   - `beamerouterthememetropolis.dtx`
   - `beamerthememetropolis.ins`
   - `pgfplotsthemetol.dtx`
   - `LICENSE`（MIT、CTAN 同梱物）

2. すべて本ディレクトリ直下に置く。

3. `skeleton/main.tex.template` の `\usetheme{metropolis}` の手前で
   `\usepackage{../../framework/templates/slide-tex/assets/metropolistheme/beamerthememetropolis}` 等を
   読むように差し替えるか、`texmf` ツリーに登録して通常のパッケージ解決に乗せる。

4. ライセンス（MIT）の保持義務に従い、`LICENSE` ファイルを **削除しない**。

ベンダリングは任意作業。TeX Live のメンテナンスに乗ったまま運用する場合は、本ディレクトリは
README のみで構わない。
