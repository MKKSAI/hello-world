{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "gpuType": "T4",
      "authorship_tag": "ABX9TyNYTyjtpHuf1Q08hNhmN8N2",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    },
    "accelerator": "GPU"
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/MKKSAI/hello-world/blob/master/ver4_pipeline.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Create ver4_pipeline.py next to your notebook\n",
        "code = r\"\"\"\n",
        "# <<< PASTE THE FULL 'ver4_pipeline.py' CODE I SENT EARLIER HERE >>>\n",
        "\"\"\"\n",
        "with open(\"ver4_pipeline.py\", \"w\", encoding=\"utf-8\") as f:\n",
        "    f.write(code)\n",
        "\n",
        "import os\n",
        "print(\"Saved:\", os.path.abspath(\"ver4_pipeline.py\"))\n"
      ],
      "metadata": {
        "id": "1XEHwuLfcnjJ",
        "outputId": "0b4a4571-f63f-4366-b98d-9a4e5a53027d",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Saved: /content/ver4_pipeline.py\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import sys, os\n",
        "sys.path.append(os.getcwd())  # ensure current dir is on sys.path\n",
        "\n",
        "from ver4_pipeline import run_pipeline_nb\n",
        "\n",
        "run_pipeline_nb(\n",
        "    reviews=\"/content/ChatGPT_Reviews_user satisfaction ratings_opendatabay.csv\",\n",
        "    traffic=\"/content/traffic_aggregated_clean_2024_2025.xlsx\",\n",
        "    trends=\"/content/trends_aggregated_clean_2024_2025.xlsx\",\n",
        "    splits=5, seed=42, min_group=30\n",
        ")\n"
      ],
      "metadata": {
        "id": "T91W8p49czub",
        "outputId": "75975a16-cfaf-400d-c4b0-e5bef8c28281",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 401
        }
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "error",
          "ename": "ImportError",
          "evalue": "cannot import name 'run_pipeline_nb' from 'ver4_pipeline' (/content/ver4_pipeline.py)",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mImportError\u001b[0m                               Traceback (most recent call last)",
            "\u001b[0;32m/tmp/ipython-input-4170967572.py\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0msys\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpath\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mappend\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mos\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mgetcwd\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m  \u001b[0;31m# ensure current dir is on sys.path\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 4\u001b[0;31m \u001b[0;32mfrom\u001b[0m \u001b[0mver4_pipeline\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mrun_pipeline_nb\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      5\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      6\u001b[0m run_pipeline_nb(\n",
            "\u001b[0;31mImportError\u001b[0m: cannot import name 'run_pipeline_nb' from 'ver4_pipeline' (/content/ver4_pipeline.py)",
            "",
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0;32m\nNOTE: If your import is failing due to a missing package, you can\nmanually install dependencies using either !pip or !apt.\n\nTo view examples of installing some common dependencies, click the\n\"Open Examples\" button below.\n\u001b[0;31m---------------------------------------------------------------------------\u001b[0m\n"
          ],
          "errorDetails": {
            "actions": [
              {
                "action": "open_url",
                "actionText": "Open Examples",
                "url": "/notebooks/snippets/importing_libraries.ipynb"
              }
            ]
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import importlib.util, types\n",
        "\n",
        "module_path = \"/content/ver4_pipeline.py\"   # <-- change if saved elsewhere\n",
        "spec = importlib.util.spec_from_file_location(\"ver4_pipeline\", module_path)\n",
        "ver4_pipeline = importlib.util.module_from_spec(spec)\n",
        "spec.loader.exec_module(ver4_pipeline)      # executes the file\n",
        "\n",
        "# now call the function from the loaded module object\n",
        "ver4_pipeline.run_pipeline_nb(\n",
        "    reviews=\"/content/ChatGPT_Reviews_user satisfaction ratings_opendatabay.csv\",\n",
        "    traffic=\"/content/traffic_aggregated_clean_2024_2025.xlsx\",\n",
        "    trends=\"/content/trends_aggregated_clean_2024_2025.xlsx\",\n",
        "    splits=5, seed=42, min_group=30\n",
        ")\n"
      ],
      "metadata": {
        "id": "6nqzvswHc8uI",
        "outputId": "b87ac411-3ffc-4076-d4d7-e22c1cca5e1d",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 228
        }
      },
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "error",
          "ename": "AttributeError",
          "evalue": "module 'ver4_pipeline' has no attribute 'run_pipeline_nb'",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
            "\u001b[0;32m/tmp/ipython-input-3308351119.py\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      7\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      8\u001b[0m \u001b[0;31m# now call the function from the loaded module object\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 9\u001b[0;31m ver4_pipeline.run_pipeline_nb(\n\u001b[0m\u001b[1;32m     10\u001b[0m     \u001b[0mreviews\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m\"/content/ChatGPT_Reviews_user satisfaction ratings_opendatabay.csv\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     11\u001b[0m     \u001b[0mtraffic\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m\"/content/traffic_aggregated_clean_2024_2025.xlsx\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mAttributeError\u001b[0m: module 'ver4_pipeline' has no attribute 'run_pipeline_nb'"
          ]
        }
      ]
    }
  ]
}