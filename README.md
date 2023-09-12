<div id="top"></div>
<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Mhackiori/EISthentication">
    <img src="https://i.postimg.cc/YSzhs6yR/EISthentication.png" alt="Logo" width="500" height="100">
  </a>

  <h1 align="center">Your Battery Is A Blast!</h1>

  <p align="center">Safeguarding Against Counterfeit Batteries with Authentication
    <br />
    <a href="https://arxiv.org/abs/2309.03607"><strong>Preprint available »</strong></a>
    <br />
    <br />
    <a href="https://www.math.unipd.it/~fmarchio/">Francesco Marchiori</a>
    ·
    <a href="https://www.math.unipd.it/~conti/">Mauro Conti</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary><strong>Table of Contents</strong></summary>
  <ol>
    <li>
      <a href="#abstract">Abstract</a>
    </li>
    <li>
      <a href="#citation">Citation</a>
    </li>
    <li>
      <a href="#usage">Usage</a>
    </li>
    <li>
      <a href="#flowchart">Flowchart</a>
    </li>
    <li>
      <a href="#datasets">Datasets</a>
    </li>
    <li>
      <a href="#models">Models</a>
    </li>
  </ol>
</details>

<div id="abstract"></div>

## 🧩 Abstract

>Lithium-ion (Li-ion) batteries are the primary power source in various applications due to their high energy and power density. Their market was estimated to be up to 48 billion U.S. dollars in 2022. However, the widespread adoption of Li-ion batteries has resulted in counterfeit cell production, which can pose safety hazards to users. Counterfeit cells can cause explosions or fires, and their prevalence in the market makes it difficult for users to detect fake cells. Indeed, current battery authentication methods can be susceptible to advanced counterfeiting techniques and are often not adaptable to various cells and systems. In this paper, we improve the state of the art on battery authentication by proposing two novel methodologies, **DCAuth** and **EISthentication**, which leverage the internal characteristics of each cell through Machine Learning models. Our methods automatically authenticate lithium-ion battery models and architectures using data from their regular usage without the need for any external device. They are also resilient to the most common and critical counterfeit practices and can scale to several batteries and devices. To evaluate the effectiveness of our proposed methodologies, we analyze time-series data from a total of 20 datasets that we have processed to extract meaningful features for our analysis. Our methods achieve high accuracy in battery authentication for both architectures (up to 0.99) and models (up to 0.96). Moreover, our methods offer comparable identification performances. By using our proposed methodologies, manufacturers can ensure that devices only use legitimate batteries, guaranteeing the operational state of any system and safety measures for the users.

<p align="right"><a href="#top">(back to top)</a></p>
<div id="citation"></div>

## 🗣️ Citation

Please, cite this work when reffering to EISthentication.

```
@article{marchiori2023your,
  title={Your Battery Is a Blast! Safeguarding Against Counterfeit Batteries with Authentication},
  author={Marchiori, Francesco and Conti, Mauro},
  journal={arXiv preprint arXiv:2309.03607},
  year={2023}
}
```

<p align="right"><a href="#top">(back to top)</a></p>
<div id="usage"></div>

## ⚙️ Usage

First, start by cloning the repository.

```bash
git clone https://github.com/Mhackiori/EISthentication.git
cd EISthentication
```

Then, install the required Python packages by running:

```bash
pip install -r requirements.txt
```

You now need to add the datasets in the repository. You can do this by downloading the zip file [here](https://figshare.com/s/db190b8462d51b744390) and extracting it in this repository.

To replicate the results in our paper, you simply need to execute the [Jupyter Notebook](https://github.com/Mhackiori/EISthentication/blob/main/EISthentication.ipynb).

<p align="right"><a href="#top">(back to top)</a></p>
<div id="flowchart"></div>

## 🚥 Flowchart

In the next Figure, we summarize the functioning of the whole system by showing a flowchart of the different steps happening before the authentication response.

![Flowchart](https://i.postimg.cc/KzDMRcPL/04-Flowchart-1.png "Flowchart")

<p align="right"><a href="#top">(back to top)</a></p>
<div id="datasets"></div>

## 📚 Datasets

Here is the list of the datasets used for EISthentication.

| **Name** | **Battery** | **Data** |
|---|---|---|
| SiCWell [[Ref]](https://ieee-dataport.org/open-access/sicwell-dataset) | Unknown (NMC) | Cycled with driving profiles (sWLTP, UDDS). |
| SNL [[Ref]](https://www.sandia.gov/ess/tools-resources/rd-data-repository) | • LGDBHE21865 (NMC)<br>• ANR18650M1 (LFP)<br>• NCR18650A (LCO)<br>• LGDBHG21865 (NCA) | Cycled at same SOC, different temperatures. |
| Zhang et al. [[Ref]](https://zenodo.org/record/3633835#.ZFDKEXZBwQ8) | Eunicell LR2032 (LCO) | Three temperatures at nine different stages of cycling. |

<p align="right"><a href="#top">(back to top)</a></p>
<div id="models"></div>

## 🤖 Models

Here is the list of the models used for EISthentication and their hyperparameters tuned during Grid Search.

| **Models** | **Hyperparameters** |
|---|---|
| AdaBoost (AB) | • Number of estimators |
| Decision Tree (DT) | • Criterion<br>• Maximum Depth |
| Gaussian Naive Bayes (GNB) | • Variance Smoothing |
| Nearest Neighbors (KNN) | • Number of neighbors<br>• Weight function |
| Neural Network (NN) | • Hidden layer sizes<br>• Activation function<br>• Solver |
| Quadratic Discriminant Analysis (QDA) | • Regularization Parameter |
| Random Forest (RF) | • Criterion<br>• Number of estimators |
| Support Vector Machine (SVM) | • Kernel<br>• Regularization parameter<br>• Kernel coefficient |

<p align="right"><a href="#top">(back to top)</a></p>