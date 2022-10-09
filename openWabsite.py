#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 21:06:43 2022

@author: JXu
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from sys import platform
from tqdm import tqdm
import json
import getopt
import sys
import time
import pandas as pd

import csv
def openChromeDriver():
    # Open chromedriver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--log-level=3')
    
    #chrome_options.add_argument("blink-settings=imagesEnabled=false")
    if platform == "linux":
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--single-process')
        chrome_options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome("./chromedriver", chrome_options=chrome_options)
    return driver

def getReviewer1(html, driver, number):
    #driver = openChromeDriver()
    stringarr = html.split("/")
    thisyear = stringarr[len(stringarr)-1]
    first_html = html +"/ratings/?pagestop"
    print(first_html)
  

def getReviewer(html, driver, number):
    #driver = openChromeDriver()
    stringarr = html.split("/")
    thisyear = stringarr[len(stringarr)-1]
    first_html = html +"/ratings/?pagestop"
    print(first_html)
    driver.get(first_html)
    time.sleep(3)
    sorry_ele = driver.find_elements_by_id("content")
    if len(sorry_ele) > 0:
        
        driver.get(first_html)
        time.sleep(3)
        sorry_ele = driver.find_elements_by_id("content")
        if len(sorry_ele) > 0:
                cur = {}
                cur["closed"] = number
                with open("record.csv", 'a+') as csvfile:
        
        
                    writer = csv.DictWriter(csvfile, fieldnames = ["no_html","closed"])
      
                    writer.writerow(cur)
                    print("{number} is closed".format(number = number))
                return
            
  
    #sorry_content =         
        
    #driver.get("https://www.consumerreports.org/cars/acura/mdx/2022/ratings/?pagestop")
    #driver.get("https://www.consumerreports.org/cars/audi/a4/2022/reliability/?pagestop")
    time.sleep(6)
    # signButton = driver.find_element_by_class_name("gnav-sign-in")
    # signButton.click()
    # time.sleep(4)
    
    # searchbox1 = driver.find_element_by_name("userName")
    # searchbox1.send_keys("jxx170330@utdallas.edu")
    # searchbox2 = driver.find_element_by_name("password")
    # searchbox2.send_keys("19900723Xjd")
    
    # searchbutton = driver.find_element_by_class_name("gnav-button.gnav-filled")
    
    # searchbutton.click()
  
    time.sleep(10)
    dic= {}
    dic["url"] = html
    dic["index"] = number
    overallscore = driver.find_elements_by_class_name("crux-numbers.overall-score-circle__value")
    name  = driver.find_element_by_class_name("crux-page-title").text.strip()
    dic["name"] = name
    print("First part")
    if len(overallscore) != 0:
        if overallscore[0].get_attribute("innerHTML").strip() != "NA":
            dic["overallscore"]=overallscore[0].get_attribute("innerHTML").strip()
    
    body_scores_name = driver.find_elements_by_class_name("crux-label-style.ratings-trim-label")
   
    body_scores = driver.find_elements_by_class_name("ratings-bar-chart")
    
    small_buttons = driver.find_elements_by_class_name("ratings-collapse__arrow")
    for i in range(1, len(small_buttons)):
        small_buttons[i].click()
    for i in range (0, len(body_scores_name)):
        if body_scores[i].text.strip() != "NA" and body_scores_name[i].text.strip() != '':
            dic[body_scores_name[i].text.strip()] = body_scores[i].text.strip().replace("/", "#")
        
    labels = driver.find_elements_by_class_name("col-xs-12.col-sm-6.col-lg-4.crux-label-style.ratings-row__label")
    
    values = driver.find_elements_by_class_name("col-xs-12.col-sm-6.col-lg-4.ratings-row__values")


    for i in range(0,len(labels)):
        if len(values[i].text)>0 and labels[i].text.strip() != '':
            
           dic[labels[i].text.strip()] = values[i].text.strip().replace("/", "#")
        
     
    small_labels = driver.find_elements_by_class_name("col-xs-12.col-sm-6.col-lg-4.ratings-sub-row__label")
    small_values = driver.find_elements_by_class_name("col-xs-12.col-sm-6.col-lg-4.ratings-sub-row__values")
    for i in range(len(small_labels)):
        if len(small_values[i].text.strip()) > 0  and small_labels[i].text.strip() != '':
           dic[small_labels[i].text.strip()] =  small_values[i].text.strip().replace("/", "#")
   
    print("Second part")
    second_html = html +"/reliability/?pagestop"
    try:
        driver.get(second_html)
    except:
        time.sleep(4)
        driver.get(second_html)
        
    sorry_ele = driver.find_elements_by_id("content")
    if len(sorry_ele) > 0:
        
        driver.get(second_html)
        time.sleep(3)
        sorry_ele = driver.find_elements_by_id("content")
        if len(sorry_ele) > 0:
                cur = {}
                cur["closed"] = number
                with open("record.csv", 'a+') as csvfile:
        
        
                    writer = csv.DictWriter(csvfile, fieldnames = ["no_html","closed"])
      
                    writer.writerow(cur)
                    print("{number} is closed".format(number = number))
                return       
    #driver.get(second_html)
    #driver.get("https://www.consumerreports.org/cars/acura/mdx/2022/reliability/?pagestop")
    time.sleep(5)
    second_page_button = driver.find_elements_by_class_name("crux-btn.crux-btn-primary--lg")
    if len(second_page_button) > 0:
        second_page_button[0].click()
    # try:
    #      second_page_button.click()
    # except:
    #     print("there is no button")
         
    time.sleep(3)
    
    reliability_name = driver.find_elements_by_class_name("reliability-score__label.crux-component-title")
    reliability_txt = driver.find_elements_by_class_name("reliability-score__value")
    if len(reliability_name) != 0 :
        if reliability_txt[0].text.strip() != "NA" and reliability_name[0].text.strip() != '':
            dic[reliability_name[0].text.strip()] = reliability_txt[0].text.strip().replace("/", "#")
    
    reliability_labels = driver.find_elements_by_class_name("crux-body-copy.crux-body-copy--small.crux-body-copy--bold.compare-years-component__rating-label")
    reliability_years = driver.find_elements_by_class_name("rating-slider__year")
    reliability_years_values = driver.find_elements_by_class_name("rating-block__rating-item")
    compare_names = driver.find_elements_by_class_name("col-sm-3.col-xs-12")
    compare_values = driver.find_elements_by_class_name("col-sm-9.col-xs-12.compare-chart_chart-row__bar")
    print(len(compare_names))
    print(len(compare_values))
    lenrange = min(len(compare_values), 30)
    for i in range(0, lenrange):
        key1 = "Reliability_Compare_Name{x}".format(x=i+1)
        key2 = "Reliability_Compare_Value{x}".format(x=i+1)
        dic[key1] = compare_names[i+1].text.strip()
        dic[key2]= compare_values[i].text.strip()
    a = 0
    #print(len(reliability_labels))
    #print(len(reliability_years))
   # print(len(reliability_years_values))
    
    
    # for i in range(0,len(reliability_labels)):
    #     print(reliability_labels[i].get_attribute("innerHTML"))
    #     print(reliability_labels[i].text)
    if len(reliability_labels) != 0:
        for i in range(0, len(reliability_years)):
            year = reliability_years[i].get_attribute("innerHTML")
            key = ""
            if a < len(reliability_labels):
                key = reliability_labels[a].get_attribute("innerHTML").strip()
            else:
                key = "outOfRange"
           
            if year.find(thisyear) != -1:
                key = key 
            else:
                continue
       
                
                
            value = "NA"
            html_txt = reliability_years_values[i].get_attribute("innerHTML")
            if html_txt.find("verygood") != -1:
                value = "verygood"
            elif html_txt.find("good") != -1:
                value = "good"
            elif html_txt.find("excellent") != -1:
                value = "excellent"
            elif html_txt.find("fair") != -1:
                value = "fair"
            elif html_txt.find("poor") != -1:
                value = "poor"
            dic[key] = value
         
            a = a+1
    second_page_button_recalls = driver.find_elements_by_class_name("crux-btn.crux-btn-tertiary--lg")
    if len(second_page_button_recalls) >0 :
        second_page_button_recalls[0].click()
    # try:
    #      second_page_button_recall.click()
    # except:
    #     print("there is no button")         
    
    recall_names = driver.find_elements_by_class_name("crux-article__bold-link.recalls__summary__title")
    recall_times = driver.find_elements_by_class_name("crux-body-copy.crux-body-copy--extra-small.recalls__summary__date")
    for i in range (0,len(recall_names)):
        if len(recall_names[i].text.strip()) > 0:
            key1 = "Recall_Name{x}".format(x=i+1)
            key2 = "Recall_Time{x}".format(x=i+1)
            dic[key1] = recall_names[i].text.strip()
            dic[key2]= recall_times[i].text.strip()
    #Third part
    print("Third part")
    third_html = html +"/owner-satisfaction/?pagestop"
    try:
        driver.get(third_html)
    except:
        time.sleep(4)
        driver.get(third_html)
    
    time.sleep(3)
    sorry_ele = driver.find_elements_by_id("content")
    if len(sorry_ele) > 0:
        
        driver.get(second_html)
        time.sleep(3)
        sorry_ele = driver.find_elements_by_id("content")
        if len(sorry_ele) > 0:
                cur = {}
                cur["closed"] = number
                with open("record.csv", 'a+') as csvfile:
        
        
                    writer = csv.DictWriter(csvfile, fieldnames = ["no_html","closed"])
      
                    writer.writerow(cur)
                    print("{number} is closed".format(number = number))
                return
    time.sleep(4)
    third_label =  driver.find_elements_by_class_name("section-intro__rating-title.crux-body-copy.crux-body-copy--small--bold")
    
    
    third_label_value =  driver.find_elements_by_class_name("js-bar-chart-mount")
    if len(third_label) != 0:
        if third_label_value[0].text.strip() != "NA" and third_label[0].text.strip() != '':
            dic[third_label[0].text.strip()] = third_label_value[0].text.strip().replace("/", "#")
    
    current_labels = driver.find_elements_by_class_name("surveys-verbatim__item-title.surveys-verbatim__item-title--font-large.crux-body-copy.crux-body-copy--bold") 
    current_values = driver.find_elements_by_class_name("col-md-offset-2.col-md-4.col-sm-offset-1.col-sm-5.col-xs-12")  
    for i in range(0, len(current_labels)):
        l = current_labels[i].text
        v = current_values[i].text
        if l.strip() != '':
            dic[l.strip()] = v.strip().replace("/", "#")
    compare_s_names = driver.find_elements_by_class_name("crux-body-copy.crux-body-copy--small--bold.compare-chart_chart-row-name.no-border")
    compare_s_values = driver.find_elements_by_class_name("col-sm-9.col-xs-12.compare-chart_chart-row__bar")
    print(len(compare_s_names))
    print(len(compare_s_values))
    lenrange2 =  min(30, len(compare_s_names))
    for i in range(0, lenrange2):
        key1 = "Owner_Satisfaction_Compare_Name{x}".format(x=i+1)
        key2 = "Owner_Satisfaction_Compare_Value{x}".format(x=i+1)
        dic[key1] = compare_s_names[i].text.strip()
        dic[key2]= compare_s_values[i].text.strip()
    #print(dic)
    field_file = open('fields.txt', 'r')
    FLines = field_file.readlines()
    fields = [];
    for l in FLines:
        fields.append(l.strip())
    with open("result0204.csv", 'a+') as csvfile:
        
        
        writer = csv.DictWriter(csvfile, fieldnames = fields)
        if number == 1:
            writer.writeheader()
      
       
        # writing data rows
        writer.writerow(dic)
        print("{number} is OK".format(number = number))
        #print("OK")
 
        
        
   



    

if __name__ == "__main__":
      
    htmlarray = []
    with open("modelyearurl.csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            html = row[4]
            htmlarray.append(html)

    driver = openChromeDriver()
        #driver.get(first_html)
    driver.get("https://www.consumerreports.org/cars/acura/mdx/2022/ratings/?pagestop")
    #driver.get("https://www.consumerreports.org/cars/audi/a4/2022/reliability/?pagestop")
    time.sleep(6)
    signButton = driver.find_element_by_class_name("gnav__sign-in")
    signButton.click()
    time.sleep(4)
    searchbox1 = driver.find_element_by_name("userName")
    searchbox1.send_keys("XXXXX.edu")
    searchbox2 = driver.find_element_by_name("password")
    searchbox2.send_keys("XXXXX")
    
    searchbutton = driver.find_element_by_class_name("gnav-button.gnav-filled")
    
    searchbutton.click()
    
    time.sleep(10)
    #getReviewer("https://www.consumerreports.org/cars/acura/ilx/2015", driver, 500)  
    #for i in range(0, len(htmlarray)):
    for i in range(1, 10):
            if len(htmlarray[i]) != 0:
                getReviewer(htmlarray[i], driver, i)
                print(htmlarray[i])
            else:
                cur = {}
                cur["no_html"] = i
                with open("record.csv", 'a+') as csvfile:
        
        
                    writer = csv.DictWriter(csvfile, fieldnames = ["no_html","closed"])
      
                    writer.writerow(cur)
                    print("no_html:")
                    print(i)
                    
    # for i in range(1, 2):
    #         if len(htmlarray[i]) != 0:
    #             getReviewer1(htmlarray[i], driver, i)
    #             #print(htmlarray[i])
    #         else:
    #             cur = {}
    #             cur["no_html"] = i
    #             with open("record.csv", 'a+') as csvfile:
        
        
    #                 writer = csv.DictWriter(csvfile, fieldnames = ["no_html","closed"])
      
    #                 writer.writerow(cur)
    #                 print("no_html:")
    #                 print(i)
 
                
    