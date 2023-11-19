# はじめに
MIDI BABELは、音源ごとのキーマップを設定し、音源間のキーマップの違いに合わせて相互変換するソフトです。ドラム音源やサンプラーへの利用を想定しています。

また、MIDI BABELは無料のオープンソースソフトウェアです。
作りとしては出来るだけシンプルに、汎用性を高くすることを意識しています。
pythonでコーディングしているため、必要であればユーザ側で改変して利用することも可能です。

# 使い方
## インストール
以下のurlから、最新のリリースファイルをダウンロードしてください。  
`https://github.com/YuNakas/midi_babel/releases`

![image](https://github.com/YuNakas/midi_babel/assets/88542340/c5d61915-c2bc-45b3-bf45-46e829f46fad)

ダウンロードしたzipファイルを解凍し、内包されている`midi_babel.exe`をダブルクリックすることでアプリケーションを起動できます。(※ 初回起動時に警告が表示されることがありますが、許可することで、次回以降は表示されなくなります。)

## トップ画面
![image](https://github.com/YuNakas/midi_babel/assets/88542340/a9bfe8a1-413d-4c49-82d6-858190b12d94)

トップ画面からは以下の機能を選択できます。機能の詳細は各画面で改めて説明します。
- MIDI変換
  - 本アプリのメイン機能です。設定したキーマッピングファイルに従って、MIDIノートの音階を書き換えます。
- オマケ機能
  - MIDI変換のうち、個人的に欲しかった機能を 3 つ用意しました。
- ファイルの保存・取込
  - 設定ファイルのインポート・エクスポートや、過去に変換したmidiファイルをもう一度保存することができます。

## MIDI変換機能
### MIDI選択画面
![image](https://github.com/YuNakas/midi_babel/assets/88542340/6b6bcebd-dc75-4b21-b28c-c3bb539f6711)

画面左上のボタンから変換したいMIDIファイルを取り込んで、ファイル名を左クリックで選択します。

---
### MIDIトラック選択画面
![image](https://github.com/YuNakas/midi_babel/assets/88542340/1d46eed8-04ea-4120-84a3-5030255d14d5)

変換したいトラックを選択します。
- メロディトラックとして選択
  - 音階楽器(ギターやボーカル、ベースなど)を変換する際はこちらをクリックします。
- リズムトラックとして選択
  - 非音階楽器(ドラムやパーカッションなど)を変換する際はこちらをクリックします。

> ※ メロディトラック/リズムトラックの選択について
> 
> 本機能は、楽譜ソフトへの取込時に支障をきたさないように搭載している機能となります。  
> midiデータはチャンネル番号を持っており、リズム楽器は通常 9 と 10 のチャンネルが割り当てられています。  
> メロディトラックを選択した場合はチャンネル番号の変換はなく、  
> リズムトラックを選択した場合はチャンネル番号を 9 に変換する処理をあわせて実施します。

---
### MIDI変換元/変換先 選択画面
![image](https://github.com/YuNakas/midi_babel/assets/88542340/81d7add8-bcf0-4ae7-a545-cfb0279bc374)

変換元/変換先のキーマッピングを設定したファイルを選択します。  
すでにキーマッピング設定ファイルが存在する場合、`選択`ボタンをクリックします。  
キーマッピング設定ファイルを編集したい場合、`編集`ボタンをクリックします。  
キーマッピング設定ファイルが存在しない場合、左上の`新規作成`ボタンをクリックします。

---
### キーマッピング設定ファイル名称設定画面
![image](https://github.com/YuNakas/midi_babel/assets/88542340/27d99d1f-bd65-4b42-a06e-9c5e484a4c18)

キーマッピング設定ファイルのファイル名を設定します。

---
### キーマッピング設定ファイル編集画面
![image](https://github.com/YuNakas/midi_babel/assets/88542340/51ce3109-8955-4bf4-8e4c-3f3ea8d1bfa1)

キーマッピングを編集します。  
`kick_hit`や`hihat_closed`など、キーの名称を左上のテキストボックスに入力して、`追加`ボタンをクリックします。  
音階に対応したノートナンバーを入力します。
> ※ 音階の表示について
> 
> 通常、midiの音階は `アルファベット` + `数字` の形で表す `音名` を用います。  
> しかし、記法によって最低音が `C-1` の場合と `C-2` の場合があるため、  
> より厳格な仕様である**ノートナンバー**を利用しています。  
> 音名とノートナンバーの対応表は本マニュアルの最下部に記載しています。

> 優先ノート と ノート一覧 について
>
> ドラム音源によっては、同じ音に対して複数の音階が割り当てられていることがあります。  
> 例えば、EzDrummer3では、snare の center に対して `D1(38)` と `F#3(66)` が割り当てられています。  
> その場合、`38` と `66` を**ノート一覧**に記述します。  
> また、そのうち、優先して利用したいものを一つだけ選んで、**優先ノート**に記述します。  

入力中は、こまめに右上の`保存`ボタンをクリックすることをおすすめします。  
入力が完了したら、右上の`この内容で決定する`ボタンをクリックします。  

---
### 変換表生成画面
![image](https://github.com/YuNakas/midi_babel/assets/88542340/b7953830-fe6a-4594-972b-458b3da2db18)

変換元のキー名を、変換先のどのキーに割り当てるかを設定する画面です。

右側のドロップダウンをクリックして変換先キー名を選択します。キー名は重複しても問題ありません。  
選択が完了したら、左上の`決定`ボタンをクリックします。

---
### 変換完了画面
![image](https://github.com/YuNakas/midi_babel/assets/88542340/129ff1c0-e8b9-4abe-ad85-dce3b372d951)

`MIDIエクスポート`ボタンをクリックすると、変換後のMIDIファイルが保存できます。  
`Topへ戻る`ボタンをクリックすると、トップ画面に戻ります。

---
## オマケ機能
### 変換モード選択画面
![image](https://github.com/YuNakas/midi_babel/assets/88542340/687927fb-86ae-455f-b2bd-816c029b64d0)

- Tautology
  - 音階を変更せずにmidiファイルを出力します。midiファイルから1トラックだけ抽出したいときなどに使います。
- Octave Up/Down
  - 音階を1オクターブ上げ下げします。

---
## ファイルの保存・取込
### インポート・エクスポート選択画面
![image](https://github.com/YuNakas/midi_babel/assets/88542340/09eaa7c6-6f08-47a3-b334-75291967df6b)

- 設定ファイルをエクスポート
  - 作成したキーマッピング設定ファイルなどをエクスポートします。本ソフトウェアのバージョンを上げる際などに使います。
- 設定ファイルをインポート
  - 前項の`設定ファイルをエクスポート`でエクスポートしたファイルをインポートします。本ソフトウェアのバージョンを上げる際などに使います。
- 変換済みmidiファイルをエクスポート
  - 過去に生成した変換後midiファイルを保存します。

---
# 音名とノートナンバーの対応表
<table>
<thead>
<tr>
<th style="text-align:center">最低音が C-2 の場合</th>
<th style="text-align:center">最低音が C-1 の場合</th>
<th style="text-align:center">ノートナンバー</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center">C-2</td>
<td style="text-align:center">C-1</td>
<td style="text-align:center">0</td>
</tr>
<tr>
<td style="text-align:center">C#-2</td>
<td style="text-align:center">C#-1</td>
<td style="text-align:center">1</td>
</tr>
<tr>
<td style="text-align:center">D-2</td>
<td style="text-align:center">D-1</td>
<td style="text-align:center">2</td>
</tr>
<tr>
<td style="text-align:center">D#-2</td>
<td style="text-align:center">D#-1</td>
<td style="text-align:center">3</td>
</tr>
<tr>
<td style="text-align:center">E-2</td>
<td style="text-align:center">E-1</td>
<td style="text-align:center">4</td>
</tr>
<tr>
<td style="text-align:center">F-2</td>
<td style="text-align:center">F-1</td>
<td style="text-align:center">5</td>
</tr>
<tr>
<td style="text-align:center">F#-2</td>
<td style="text-align:center">F#-1</td>
<td style="text-align:center">6</td>
</tr>
<tr>
<td style="text-align:center">G-2</td>
<td style="text-align:center">G-1</td>
<td style="text-align:center">7</td>
</tr>
<tr>
<td style="text-align:center">G#-2</td>
<td style="text-align:center">G#-1</td>
<td style="text-align:center">8</td>
</tr>
<tr>
<td style="text-align:center">A-2</td>
<td style="text-align:center">A-1</td>
<td style="text-align:center">9</td>
</tr>
<tr>
<td style="text-align:center">A#-2</td>
<td style="text-align:center">A#-1</td>
<td style="text-align:center">10</td>
</tr>
<tr>
<td style="text-align:center">B-2</td>
<td style="text-align:center">B-1</td>
<td style="text-align:center">11</td>
</tr>
<tr>
<td style="text-align:center">C-1</td>
<td style="text-align:center">C0</td>
<td style="text-align:center">12</td>
</tr>
<tr>
<td style="text-align:center">C#-1</td>
<td style="text-align:center">C#0</td>
<td style="text-align:center">13</td>
</tr>
<tr>
<td style="text-align:center">D-1</td>
<td style="text-align:center">D0</td>
<td style="text-align:center">14</td>
</tr>
<tr>
<td style="text-align:center">D#-1</td>
<td style="text-align:center">D#0</td>
<td style="text-align:center">15</td>
</tr>
<tr>
<td style="text-align:center">E-1</td>
<td style="text-align:center">E0</td>
<td style="text-align:center">16</td>
</tr>
<tr>
<td style="text-align:center">F-1</td>
<td style="text-align:center">F0</td>
<td style="text-align:center">17</td>
</tr>
<tr>
<td style="text-align:center">F#-1</td>
<td style="text-align:center">F#0</td>
<td style="text-align:center">18</td>
</tr>
<tr>
<td style="text-align:center">G-1</td>
<td style="text-align:center">G0</td>
<td style="text-align:center">19</td>
</tr>
<tr>
<td style="text-align:center">G#-1</td>
<td style="text-align:center">G#0</td>
<td style="text-align:center">20</td>
</tr>
<tr>
<td style="text-align:center">A-1</td>
<td style="text-align:center">A0</td>
<td style="text-align:center">21</td>
</tr>
<tr>
<td style="text-align:center">A#-1</td>
<td style="text-align:center">A#0</td>
<td style="text-align:center">22</td>
</tr>
<tr>
<td style="text-align:center">B-1</td>
<td style="text-align:center">B0</td>
<td style="text-align:center">23</td>
</tr>
<tr>
<td style="text-align:center">C0</td>
<td style="text-align:center">C1</td>
<td style="text-align:center">24</td>
</tr>
<tr>
<td style="text-align:center">C#0</td>
<td style="text-align:center">C#1</td>
<td style="text-align:center">25</td>
</tr>
<tr>
<td style="text-align:center">D0</td>
<td style="text-align:center">D1</td>
<td style="text-align:center">26</td>
</tr>
<tr>
<td style="text-align:center">D#0</td>
<td style="text-align:center">D#1</td>
<td style="text-align:center">27</td>
</tr>
<tr>
<td style="text-align:center">E0</td>
<td style="text-align:center">E1</td>
<td style="text-align:center">28</td>
</tr>
<tr>
<td style="text-align:center">F0</td>
<td style="text-align:center">F1</td>
<td style="text-align:center">29</td>
</tr>
<tr>
<td style="text-align:center">F#0</td>
<td style="text-align:center">F#1</td>
<td style="text-align:center">30</td>
</tr>
<tr>
<td style="text-align:center">G0</td>
<td style="text-align:center">G1</td>
<td style="text-align:center">31</td>
</tr>
<tr>
<td style="text-align:center">G#0</td>
<td style="text-align:center">G#1</td>
<td style="text-align:center">32</td>
</tr>
<tr>
<td style="text-align:center">A0</td>
<td style="text-align:center">A1</td>
<td style="text-align:center">33</td>
</tr>
<tr>
<td style="text-align:center">A#0</td>
<td style="text-align:center">A#1</td>
<td style="text-align:center">34</td>
</tr>
<tr>
<td style="text-align:center">B0</td>
<td style="text-align:center">B1</td>
<td style="text-align:center">35</td>
</tr>
<tr>
<td style="text-align:center">C1</td>
<td style="text-align:center">C2</td>
<td style="text-align:center">36</td>
</tr>
<tr>
<td style="text-align:center">C#1</td>
<td style="text-align:center">C#2</td>
<td style="text-align:center">37</td>
</tr>
<tr>
<td style="text-align:center">D1</td>
<td style="text-align:center">D2</td>
<td style="text-align:center">38</td>
</tr>
<tr>
<td style="text-align:center">D#1</td>
<td style="text-align:center">D#2</td>
<td style="text-align:center">39</td>
</tr>
<tr>
<td style="text-align:center">E1</td>
<td style="text-align:center">E2</td>
<td style="text-align:center">40</td>
</tr>
<tr>
<td style="text-align:center">F1</td>
<td style="text-align:center">F2</td>
<td style="text-align:center">41</td>
</tr>
<tr>
<td style="text-align:center">F#1</td>
<td style="text-align:center">F#2</td>
<td style="text-align:center">42</td>
</tr>
<tr>
<td style="text-align:center">G1</td>
<td style="text-align:center">G2</td>
<td style="text-align:center">43</td>
</tr>
<tr>
<td style="text-align:center">G#1</td>
<td style="text-align:center">G#2</td>
<td style="text-align:center">44</td>
</tr>
<tr>
<td style="text-align:center">A1</td>
<td style="text-align:center">A2</td>
<td style="text-align:center">45</td>
</tr>
<tr>
<td style="text-align:center">A#1</td>
<td style="text-align:center">A#2</td>
<td style="text-align:center">46</td>
</tr>
<tr>
<td style="text-align:center">B1</td>
<td style="text-align:center">B2</td>
<td style="text-align:center">47</td>
</tr>
<tr>
<td style="text-align:center">C2</td>
<td style="text-align:center">C3</td>
<td style="text-align:center">48</td>
</tr>
<tr>
<td style="text-align:center">C#2</td>
<td style="text-align:center">C#3</td>
<td style="text-align:center">49</td>
</tr>
<tr>
<td style="text-align:center">D2</td>
<td style="text-align:center">D3</td>
<td style="text-align:center">50</td>
</tr>
<tr>
<td style="text-align:center">D#2</td>
<td style="text-align:center">D#3</td>
<td style="text-align:center">51</td>
</tr>
<tr>
<td style="text-align:center">E2</td>
<td style="text-align:center">E3</td>
<td style="text-align:center">52</td>
</tr>
<tr>
<td style="text-align:center">F2</td>
<td style="text-align:center">F3</td>
<td style="text-align:center">53</td>
</tr>
<tr>
<td style="text-align:center">F#2</td>
<td style="text-align:center">F#3</td>
<td style="text-align:center">54</td>
</tr>
<tr>
<td style="text-align:center">G2</td>
<td style="text-align:center">G3</td>
<td style="text-align:center">55</td>
</tr>
<tr>
<td style="text-align:center">G#2</td>
<td style="text-align:center">G#3</td>
<td style="text-align:center">56</td>
</tr>
<tr>
<td style="text-align:center">A2</td>
<td style="text-align:center">A3</td>
<td style="text-align:center">57</td>
</tr>
<tr>
<td style="text-align:center">A#2</td>
<td style="text-align:center">A#3</td>
<td style="text-align:center">58</td>
</tr>
<tr>
<td style="text-align:center">B2</td>
<td style="text-align:center">B3</td>
<td style="text-align:center">59</td>
</tr>
<tr>
<td style="text-align:center">C3</td>
<td style="text-align:center">C4</td>
<td style="text-align:center">60</td>
</tr>
<tr>
<td style="text-align:center">C#3</td>
<td style="text-align:center">C#4</td>
<td style="text-align:center">61</td>
</tr>
<tr>
<td style="text-align:center">D3</td>
<td style="text-align:center">D4</td>
<td style="text-align:center">62</td>
</tr>
<tr>
<td style="text-align:center">D#3</td>
<td style="text-align:center">D#4</td>
<td style="text-align:center">63</td>
</tr>
<tr>
<td style="text-align:center">E3</td>
<td style="text-align:center">E4</td>
<td style="text-align:center">64</td>
</tr>
<tr>
<td style="text-align:center">F3</td>
<td style="text-align:center">F4</td>
<td style="text-align:center">65</td>
</tr>
<tr>
<td style="text-align:center">F#3</td>
<td style="text-align:center">F#4</td>
<td style="text-align:center">66</td>
</tr>
<tr>
<td style="text-align:center">G3</td>
<td style="text-align:center">G4</td>
<td style="text-align:center">67</td>
</tr>
<tr>
<td style="text-align:center">G#3</td>
<td style="text-align:center">G#4</td>
<td style="text-align:center">68</td>
</tr>
<tr>
<td style="text-align:center">A3</td>
<td style="text-align:center">A4</td>
<td style="text-align:center">69</td>
</tr>
<tr>
<td style="text-align:center">A#3</td>
<td style="text-align:center">A#4</td>
<td style="text-align:center">70</td>
</tr>
<tr>
<td style="text-align:center">B3</td>
<td style="text-align:center">B4</td>
<td style="text-align:center">71</td>
</tr>
<tr>
<td style="text-align:center">C4</td>
<td style="text-align:center">C5</td>
<td style="text-align:center">72</td>
</tr>
<tr>
<td style="text-align:center">C#4</td>
<td style="text-align:center">C#5</td>
<td style="text-align:center">73</td>
</tr>
<tr>
<td style="text-align:center">D4</td>
<td style="text-align:center">D5</td>
<td style="text-align:center">74</td>
</tr>
<tr>
<td style="text-align:center">D#4</td>
<td style="text-align:center">D#5</td>
<td style="text-align:center">75</td>
</tr>
<tr>
<td style="text-align:center">E4</td>
<td style="text-align:center">E5</td>
<td style="text-align:center">76</td>
</tr>
<tr>
<td style="text-align:center">F4</td>
<td style="text-align:center">F5</td>
<td style="text-align:center">77</td>
</tr>
<tr>
<td style="text-align:center">F#4</td>
<td style="text-align:center">F#5</td>
<td style="text-align:center">78</td>
</tr>
<tr>
<td style="text-align:center">G4</td>
<td style="text-align:center">G5</td>
<td style="text-align:center">79</td>
</tr>
<tr>
<td style="text-align:center">G#4</td>
<td style="text-align:center">G#5</td>
<td style="text-align:center">80</td>
</tr>
<tr>
<td style="text-align:center">A4</td>
<td style="text-align:center">A5</td>
<td style="text-align:center">81</td>
</tr>
<tr>
<td style="text-align:center">A#4</td>
<td style="text-align:center">A#5</td>
<td style="text-align:center">82</td>
</tr>
<tr>
<td style="text-align:center">B4</td>
<td style="text-align:center">B5</td>
<td style="text-align:center">83</td>
</tr>
<tr>
<td style="text-align:center">C5</td>
<td style="text-align:center">C6</td>
<td style="text-align:center">84</td>
</tr>
<tr>
<td style="text-align:center">C#5</td>
<td style="text-align:center">C#6</td>
<td style="text-align:center">85</td>
</tr>
<tr>
<td style="text-align:center">D5</td>
<td style="text-align:center">D6</td>
<td style="text-align:center">86</td>
</tr>
<tr>
<td style="text-align:center">D#5</td>
<td style="text-align:center">D#6</td>
<td style="text-align:center">87</td>
</tr>
<tr>
<td style="text-align:center">E5</td>
<td style="text-align:center">E6</td>
<td style="text-align:center">88</td>
</tr>
<tr>
<td style="text-align:center">F5</td>
<td style="text-align:center">F6</td>
<td style="text-align:center">89</td>
</tr>
<tr>
<td style="text-align:center">F#5</td>
<td style="text-align:center">F#6</td>
<td style="text-align:center">90</td>
</tr>
<tr>
<td style="text-align:center">G5</td>
<td style="text-align:center">G6</td>
<td style="text-align:center">91</td>
</tr>
<tr>
<td style="text-align:center">G#5</td>
<td style="text-align:center">G#6</td>
<td style="text-align:center">92</td>
</tr>
<tr>
<td style="text-align:center">A5</td>
<td style="text-align:center">A6</td>
<td style="text-align:center">93</td>
</tr>
<tr>
<td style="text-align:center">A#5</td>
<td style="text-align:center">A#6</td>
<td style="text-align:center">94</td>
</tr>
<tr>
<td style="text-align:center">B5</td>
<td style="text-align:center">B6</td>
<td style="text-align:center">95</td>
</tr>
<tr>
<td style="text-align:center">C6</td>
<td style="text-align:center">C7</td>
<td style="text-align:center">96</td>
</tr>
<tr>
<td style="text-align:center">C#6</td>
<td style="text-align:center">C#7</td>
<td style="text-align:center">97</td>
</tr>
<tr>
<td style="text-align:center">D6</td>
<td style="text-align:center">D7</td>
<td style="text-align:center">98</td>
</tr>
<tr>
<td style="text-align:center">D#6</td>
<td style="text-align:center">D#7</td>
<td style="text-align:center">99</td>
</tr>
<tr>
<td style="text-align:center">E6</td>
<td style="text-align:center">E7</td>
<td style="text-align:center">100</td>
</tr>
<tr>
<td style="text-align:center">F6</td>
<td style="text-align:center">F7</td>
<td style="text-align:center">101</td>
</tr>
<tr>
<td style="text-align:center">F#6</td>
<td style="text-align:center">F#7</td>
<td style="text-align:center">102</td>
</tr>
<tr>
<td style="text-align:center">G6</td>
<td style="text-align:center">G7</td>
<td style="text-align:center">103</td>
</tr>
<tr>
<td style="text-align:center">G#6</td>
<td style="text-align:center">G#7</td>
<td style="text-align:center">104</td>
</tr>
<tr>
<td style="text-align:center">A6</td>
<td style="text-align:center">A7</td>
<td style="text-align:center">105</td>
</tr>
<tr>
<td style="text-align:center">A#6</td>
<td style="text-align:center">A#7</td>
<td style="text-align:center">106</td>
</tr>
<tr>
<td style="text-align:center">B6</td>
<td style="text-align:center">B7</td>
<td style="text-align:center">107</td>
</tr>
<tr>
<td style="text-align:center">C7</td>
<td style="text-align:center">C8</td>
<td style="text-align:center">108</td>
</tr>
<tr>
<td style="text-align:center">C#7</td>
<td style="text-align:center">C#8</td>
<td style="text-align:center">109</td>
</tr>
<tr>
<td style="text-align:center">D7</td>
<td style="text-align:center">D8</td>
<td style="text-align:center">110</td>
</tr>
<tr>
<td style="text-align:center">D#7</td>
<td style="text-align:center">D#8</td>
<td style="text-align:center">111</td>
</tr>
<tr>
<td style="text-align:center">E7</td>
<td style="text-align:center">E8</td>
<td style="text-align:center">112</td>
</tr>
<tr>
<td style="text-align:center">F7</td>
<td style="text-align:center">F8</td>
<td style="text-align:center">113</td>
</tr>
<tr>
<td style="text-align:center">F#7</td>
<td style="text-align:center">F#8</td>
<td style="text-align:center">114</td>
</tr>
<tr>
<td style="text-align:center">G7</td>
<td style="text-align:center">G8</td>
<td style="text-align:center">115</td>
</tr>
<tr>
<td style="text-align:center">G#7</td>
<td style="text-align:center">G#8</td>
<td style="text-align:center">116</td>
</tr>
<tr>
<td style="text-align:center">A7</td>
<td style="text-align:center">A8</td>
<td style="text-align:center">117</td>
</tr>
<tr>
<td style="text-align:center">A#7</td>
<td style="text-align:center">A#8</td>
<td style="text-align:center">118</td>
</tr>
<tr>
<td style="text-align:center">B7</td>
<td style="text-align:center">B8</td>
<td style="text-align:center">119</td>
</tr>
<tr>
<td style="text-align:center">C8</td>
<td style="text-align:center">C9</td>
<td style="text-align:center">120</td>
</tr>
<tr>
<td style="text-align:center">C#8</td>
<td style="text-align:center">C#9</td>
<td style="text-align:center">121</td>
</tr>
<tr>
<td style="text-align:center">D8</td>
<td style="text-align:center">D9</td>
<td style="text-align:center">122</td>
</tr>
<tr>
<td style="text-align:center">D#8</td>
<td style="text-align:center">D#9</td>
<td style="text-align:center">123</td>
</tr>
<tr>
<td style="text-align:center">E8</td>
<td style="text-align:center">E9</td>
<td style="text-align:center">124</td>
</tr>
<tr>
<td style="text-align:center">F8</td>
<td style="text-align:center">F9</td>
<td style="text-align:center">125</td>
</tr>
<tr>
<td style="text-align:center">F#8</td>
<td style="text-align:center">F#9</td>
<td style="text-align:center">126</td>
</tr>
<tr>
<td style="text-align:center">G8</td>
<td style="text-align:center">G9</td>
<td style="text-align:center">127</td>
</tr>
</tbody>
</table>
