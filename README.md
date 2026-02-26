<p>
有限グラフ上の量子ウォーク（Quantum Walk）の時間発展をシミュレーションし、
その存在確率（測度）の時間推移を <strong>LSTM を用いて予測する研究プロジェクト</strong> です。
</p>

<div class="section">
<h2>研究目的</h2>
<p>
時間発展とともに変化する量子ウォーカーの位置および存在確率（測度）を
ニューラルネットワークを用いて予測することを目的としています。
</p>
</div>

<div class="section">
<h2>量子ウォークの定義</h2>

<p>
グラフ G=(V(G), E(G)) の有向辺集合 D(G) 上の複素数値関数を量子状態 Ψ とします。
</p>

<p>
時刻 n における量子状態は、ユニタリ行列 U を用いて
</p>

<p><strong>Ψ<sub>n+1</sub> = UΨ<sub>n</sub> = U<sup>n+1</sup>Ψ<sub>0</sub></strong></p>

<h3>測度（存在確率）</h3>

<ul>
<li>有向辺 e<sub>i</sub> における測度： |ψ<sub>n,e<sub>i</sub></sub>|²</li>
<li>頂点 v<sub>j</sub> における測度： v<sub>j</sub> に向かう有向辺の測度の総和</li>
</ul>
</div>

<div class="section">
<h2>実験1：有限グラフ上の量子ウォーク</h2>

<p>以下のグラフでシミュレーションを実施：</p>

<ul>
<li>閉路グラフ（C₃, C₄）</li>
<li>フレンドシップグラフ（F₃）</li>
<li>完全グラフ（K₄）</li>
<li>完全二部グラフ（K₂,₃）</li>
<li>スターグラフ（S₃）</li>
<li>フランクリングラフ</li>
<li>ピーターセングラフ</li>
</ul>
</div>

<div class="section">
<h2>実験2：ニューラルネットワークによる予測</h2>

<h3>回帰設定</h3>
<ul>
<li>入力：時刻 t-10 〜 t-1 の10個の測度</li>
<li>出力：時刻 t の測度</li>
</ul>

<h3>モデル構成</h3>
<ul>
<li>LSTM層</li>
<li>全結合層</li>
</ul>

<h3>学習設定</h3>
<ul>
<li>損失関数：Mean Squared Error (MSE)</li>
<li>最適化手法：Adam</li>
<li>学習データ : テストデータ = 8 : 2</li>
</ul>
</div>

<div class="section">
<h2>グラフの分類</h2>

<h3>タイプ1：厳密に周期回帰</h3>
<ul>
<li>閉路グラフ</li>
<li>フレンドシップグラフ</li>
<li>完全二部グラフ</li>
<li>スターグラフ</li>
</ul>

<h3>タイプ2：概ね回帰的</h3>
<ul>
<li>完全グラフ（K₃を除く）</li>
<li>フランクリングラフ</li>
</ul>

<h3>タイプ3：非回帰的</h3>
<ul>
<li>ピーターセングラフ</li>
</ul>
</div>

<div class="section">
<h2>ディレクトリ構成</h2>

<pre>
QuantumWalkPrediction
├ requirements.txt
├ README.md
└ src
  ├ dataset.py
  ├ initial_states.py
  ├ model.py
  ├ prediction_plot.py
  ├ quantum_walk.py
  ├ result_plot.py
  ├ train.py
  ├ unitary_matrixes.py
  └ prediction_result
</pre>
</div>

<div class="section">
<h2>使用方法</h2>

<h3>環境構築</h3>
<pre><code>pip install -r requirements.txt</code></pre>

<h3>量子ウォーク実行</h3>
<pre><code>python src/quantum_walk.py</code></pre>

<h3>学習実行</h3>
<pre><code>python src/train.py</code></pre>

<h3>可視化</h3>
<pre><code>python src/result_plot.py
python src/prediction_plot.py</code></pre>
</div>

<div class="section">
<h2>今後の課題</h2>
<ul>
<li>グラフ構造（頂点数・次数・有向辺数）と分類の関係性の解明</li>
<li>大規模グラフへの拡張</li>
<li>他モデル（例：Transformer）との比較</li>
</ul>
</div>

</body>
