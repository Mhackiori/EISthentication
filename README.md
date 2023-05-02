<div id="top"></div>
<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Mhackiori/EISthentication">
    <img src="https://i.postimg.cc/YSzhs6yR/EISthentication.png" alt="Logo" width="500" height="100">
  </a>

  <h1 align="center">Your Battery Is (Not) Safe</h1>

  <p align="center">Safeguarding Against Counterfeit Batteries with Authentication
    <br />
    <a href=""><strong>Paper in progress »</strong></a>
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
      <a href="#usage">Usage</a>
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

>Lithium-ion (Li-ion) batteries have become the primary power source in different domains due to their higher energy and power density. With their dominant application in mobile phones, notebooks, and, in particular, electric cars, their market in 2022 was estimated to be up to 48 billion U.S. dollars. However, the mass employment of this cell architecture is also leading to counterfeiting issues, with many third parties exaggerating their capacity, disguising compromised cells as legitimate, and ignoring safety measures to push down their price. This problem becomes particularly relevant in electric vehicles (EVs), where the proper functioning of each cell is crucial for the safety of the driver and the passengers. In this paper, we propose **DCAuth** and **EISthentication**, two novel methods for the automatic authentication of lithium-ion batteries using data retrievable from their regular usage. Without relying on any external device, our techniques are resilient to the most common and critical counterfeit practices and are scalable to several batteries and devices. Our methods can correctly identify both lithium cell architectures and cell samples using, respectively, Differential Capacity Analysis (DCA) and Electrochemical Impedance Spectroscopy (EIS). To test our proposed methodology, we collect a large number of publicly available datasets and process them to extract meaningful features from their time-series data. Both our methodologies obtain high accuracy values in the authentication of battery chemistries and battery models. With this work, manufacturers can ensure that each device is boarding a battery from a pre-defined set of authorized models, thus guaranteeing their operative state and safety measures.

<p align="right"><a href="#top">(back to top)</a></p>
<div id="usage"></div>

## ⚙️ Usage

First, start by cloning the repository.

```bash
git clone https://github.com/Mhackiori/EISthentication.git
cd EISthentication
```
<sup>NOTE: if you're accessing this data from the anonymized repository, the above command might not work. Instead, you can download the repository from [here]().</sup>

Then, install the required Python packages by running:

```bash
pip install -r requirements.txt
```

You now need to add the datasets in the repository. You can do this by downloading the zip file [here]() and extracting it in this repository.

To replicate the results in our paper, you simply need to execute the [Jupyter Notebook](https://github.com/Mhackiori/EISthentication/blob/main/EISthentication.ipynb).

<p align="right"><a href="#top">(back to top)</a></p>
<div id="datasets"></div>

## 📚 Datasets

Here is the list of the datasets used for EISthentication.

| **Name** | **Battery** | **Data** |
|---|---|---|
| SiCWell [[Ref]](https://ieee-dataport.org/open-access/sicwell-dataset) | Unknown (NMC) | Cycled with driving profiles (sWLTP, UDDS) |
| SNL [[Ref]](https://www.sandia.gov/ess/tools-resources/rd-data-repository) | LGDBHE21865 (NMC)<br>ANR18650M1 (LFP)<br>NCR18650A (LCO)<br>LGDBHG21865 (NCA) | Cycled at same SOC, different temperatures |
| Zhang et al. [[Ref]](https://zenodo.org/record/3633835#.ZFDKEXZBwQ8) | Eunicell LR2032 (LCO) | Three temperatures at nine different stages of cycling |

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