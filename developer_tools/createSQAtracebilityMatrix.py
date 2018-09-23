# Copyright 2017 Battelle Energy Alliance, LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
 Created on Jan 20, 2017

 @author: alfoa
"""
import os
from glob import glob
import inspect
import xml.etree.ElementTree as ET
import copy
import sys
from collections import OrderedDict, defaultdict
# import utility functions
import readRequirementsAndCreateLatex as readRequirements
from createRegressionTestDocumentation import testDescription as regressionTests



def contructRequirementMapWithTests(requirementDict):
  """
    Method to construct the link between requirements' ids and tests
    @ In, requirementDict, dict, the requirement dictionary 
    @ Out, reqDictionary, dict, the requirement mapping ({'req id':[test1,test2,etc]})
  """
  reqDictionary = defaultdict(list)
  for testName,req in requirementDict.items():
    for reqId in req.find("requirements").text.split():
      reqDictionary[reqId.strip()].append(testName)  
  return reqDictionary

def createLatexFile(reqDictionary,reqDocument,outputLatex):
  """
    Method to construct the link between requirements' ids and tests
    @ In, reqDictionary, dict, the requirement mapping ({'req id':[test1,test2,etc]})
    @ In, reqDocument, tuple, (app name, the requirement dictionary)
    @ In, outputLatex, string, the output latex file
    @ Out, None
  """

  fileObject = open(outputLatex,"w+")
  fileObject.write(" \\documentclass{"+documentClass+"}\n")
  for packageLatex in latexPackages: fileObject.write(" \\usepackage{"+packageLatex.strip()+"} \n")
  fileObject.write(" \\usepackage{hyperref} \n \\usepackage[automark,nouppercase]{scrpage2} \n")
  fileObject.write(" \\usepackage[obeyspaces,dvipsnames,svgnames,x11names,table,hyperref]{xcolor} \n")
  fileObject.write(" \\usepackage{times} \n \\usepackage[FIGBOTCAP,normal,bf,tight]{subfigure} \n")
  fileObject.write(" \\usepackage{amsmath} \n \\usepackage{amssymb} \n")
  fileObject.write(" \\usepackage{soul} \n \\usepackage{pifont} \n \\usepackage{enumerate} \n")
  fileObject.write(" \\usepackage{listings}  \n \\usepackage{fullpage} \n \\usepackage{xcolor} \n \\usepackage{tabularx} \n")
  fileObject.write(" \\usepackage{ifthen}  \n \\usepackage{textcomp}  \n  \\usepackage{mathtools} \n")
  fileObject.write(" \\usepackage{relsize}  \n \\usepackage{lscape}  \n \\usepackage[toc,page]{appendix} \n")
  fileObject.write("\n")
  fileObject.write(' \\lstdefinestyle{XML} {\n language=XML, \n extendedchars=true, \n breaklines=true, \n breakatwhitespace=true, \n')
  fileObject.write(' emphstyle=\color{red}, \n basicstyle=\\ttfamily, \n commentstyle=\\color{gray}\\upshape, \n ')
  fileObject.write(' morestring=[b]", \n morecomment=[s]{<?}{?>}, \n morecomment=[s][\color{forestgreen}]{<!--}{-->},')
  fileObject.write(' keywordstyle=\\color{cyan}, \n stringstyle=\\ttfamily\color{black}, tagstyle=\color{blue}\\bf \\ttfamily \n }')

  fileObject.write(" \\title{RAVEN Requirements Traceability Matrix}\n")
  fileObject.write(" \\begin{document} \n \\maketitle \n")

  app, allGroups = reqDocument
  
  for group, groupDict in allGroups.items():
    for reqSetName,reqSet in groupDict.items():
      for reqName,req in reqSet.items()
        pass
  
  reqDictionary = defaultdict(list)
  for testName,req in requirementDict.items():
    for reqId in req.find("requirements").text.split():
      reqDictionary[reqId.strip()].append(testName)  
  
  
  fileObject.close()
  
  return reqDictionary

if __name__ == '__main__':
  try:
    index = sys.argv.index("-i")
    requirementFile = sys.argv[index+1].strip()
  except ValueError:
    raise ValueError("Not found command line argument -i")
  try:
    index = sys.argv.index("-o")
    outputLatex = sys.argv[index+1].strip()
  except ValueError:
    raise ValueError("Not found command line argument -o")

  reqDocument = readRequirements.readRequirementsXml(requirementFile)
  descriptionClass = regressionTests()
  _, _, requirementDict = descriptionClass.splitTestDescription()
  reqDictionary = contructRequirementMapWithTests(requirementDict)
  createLatexFile(reqDictionary,reqDocument,outputLatex)
 











