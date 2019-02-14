#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 19:55:47 2019

@author: 278mt
"""
import re
import requests
from . import urlcode
from bs4 import BeautifulSoup

def isdoi(article):
    return (re.search("doi.*?=.*?{.*?}", article) is not None)

def getdoi(title):
    title = re.sub("[\W]+", "+", title)
    title = re.sub("\++", "+", title)
    target_url = "https://scholar.google.co.jp/scholar?q="+title
    target_html = requests.get(target_url).text
    
    soup = BeautifulSoup(target_html, "html.parser")
    
    gs_ris = soup.find_all("div", attrs={"class": "gs_ri"})
    for gs_ri in gs_ris:
        try:
            target_gs_ri_url = gs_ri.find("a").get("href")
            target_gs_ri_html = requests.get(target_gs_ri_url).text
            doiiter = re.search("https.*?doi.org.*?\"", target_gs_ri_html)
        except requests.exceptions.InvalidSchema:
            continue
        if doiiter is not None:
            doi = urlcode.decode(doiiter.group(0))
            doi = re.sub("(\"|&).*", "", doi)
            return doi
    return None

def gettitle(article):
    title = re.search("title.*?=.*?{.*?},", article).group(0)
    title = re.search("{.*?},", title).group(0)[1:-2]
    return title

def splitarticles(fname):
    file = open(fname, "r")
    target_bib = file.read()
    file.close()
    articles_iter = re.finditer("(#|@(article|inproceedings|phdthesis|masterthesis|book|incollection))(.|\s)*?\s}", target_bib)
    articles = [article_iter.group(0) for article_iter in articles_iter]
    for a in range(len(articles)):
        if not isdoi(articles[a]):
            title = gettitle(articles[a])
            print("title=\""+title+"\"のdoiを取得します")
            doi = getdoi(title)
            if doi is None:
                print(">>> DOINotFound: title=\""+title+"\"のdoiはありませんでした")
            else:
                articles[a] = articles[a][0:-1]+"  doi = {"+doi[len("https://doi.org/"):]+"}\n}\n"
    
    return articles

def loaddoi(fname, ofname="output.doi"):
    articles = splitarticles(fname)
    
    file = open(ofname, "w")
    print("ファイルを出力します")
    for article in articles:
        file.write(article+"\n\n")
    file.close()
    print("ファイルを出力しました")

if __name__ == "__main__":
    loaddoi("../mybibfile.bib", "../output.bib")