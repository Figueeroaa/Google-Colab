{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMi3Z+N+IU89fifCOrGlA4E",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Figueeroaa/Google-Colab/blob/main/ola.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "R561_7NRArOs",
        "outputId": "df287cef-7f78-497a-dcb1-2770bee56b46"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Ingrese el precio 14990\n",
            "Ingresa un descuento 30\n",
            "4497.0\n",
            "10493.0\n"
          ]
        }
      ],
      "source": [
        "precio=int(input(\"Ingrese el precio \"))\n",
        "descuento=int(input(\"Ingresa un descuento \"))\n",
        "\n",
        "resultado=precio*descuento/100\n",
        "print(resultado)\n",
        "\n",
        "ropa=precio-resultado\n",
        "print(ropa)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "precio=int(input(\"Ingrese el precio:\\n \"))\n",
        "descuento=int(input(\"Ingresa un descuento:\\n \"))\n",
        "# se realiza descuento\n",
        "resultado=precio*descuento/100\n",
        "print(resultado)\n",
        "# descuento con el precio\n",
        "precio_final=precio-resultado\n",
        "print(precio_final)\n"
      ],
      "metadata": {
        "id": "6E2NpELUpLt7"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}