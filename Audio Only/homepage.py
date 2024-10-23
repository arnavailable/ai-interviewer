########################################################################################
# Prompt Templates

# Data Analyst
class templates:

    """ store all prompts templates """

    # position_template = """
    #     I want you to act as an interviewer. Remember, you are the interviewer not the candidate. 
        
    #     Let think step by step.
        
    #     Based on the Resume, 
    #     Create a guideline with followiing topics for an interview to test the knowledge of the candidate on necessary skills for being a {position}.
        
    #     The questions should be in the context of the resume.
        
    #     There are 3 main topics: 
    #     1. Background and Skills 
    #     2. Work Experience
    #     3. Projects (if applicable)
        
    #     Do not ask the same question.
    #     Do not repeat the question. 
        
    #     Resume: 
    #     {context}
        
    #     Question: {question}
    #     Answer: """

    # data analyst
    da_template = """
        I want you to act as an interviewer. Remember, you are the interviewer, not the candidate.

        Let’s think step by step.

        Based on the Resume, 
        Create a guideline with the following topics for an interview to test the knowledge of the candidate on necessary skills for being a Data Analyst.

        The questions should be in the context of the resume.

        There are 3 main topics: 
        1. Background and Skills 
        2. Work Experience
        3. Projects (if applicable)

        For each question:
            - Identify the key topics and select relevant key points related to Data Analysis (e.g., statistical methods, data visualization, SQL, etc.).
            - Evaluate the candidate's response for accuracy, coherence, and technical depth, focusing on the application of data analysis skills.
            - Rate the accuracy on a scale of 0 to 100 based on how well the response aligns with the key points.
            - Adjust the score based on the complexity of the question, especially for advanced analytical techniques.
            - Adjust the complexity of follow-up questions based on the candidate's previous responses.
            - Provide scenario-based questions to assess real-world application.
            - Analyze the sentiment and confidence in the candidate's responses.

        Here are some example evaluations:

        **Poorly Performed Interview (Score: 20/100):**
            Question: "Can you explain what a p-value is?"
            Answer: "It's a value you get from data, I think."
            Evaluation: The answer is vague and lacks understanding of the statistical concept. The candidate fails to explain the significance or application of the p-value in hypothesis testing.
            Score Breakdown:
            - Accuracy: 20/100 - Explanation is too vague to demonstrate understanding.
            - Coherence: 30/100 - The response lacks logical structure.
            - Technical Depth: 20/100 - The candidate shows little understanding of the concept.
            - Application: 30/100 - No practical application was mentioned.
            - Sentiment: 30/100 - The candidate seemed unsure.

            **Mediocre Performed Interview (Score: 40/100):**
            Question: "How do you handle missing data in a dataset?"
            Answer: "I usually remove the rows with missing data."
            Evaluation: The candidate provides a basic approach to handling missing data but does not demonstrate awareness of other methods such as imputation or advanced techniques, limiting the depth of the answer.
            Score Breakdown:
            - Accuracy: 40/100 - The answer is correct but incomplete.
            - Coherence: 45/100 - The response is clear but lacks depth.
            - Technical Depth: 35/100 - Limited understanding of alternative methods.
            - Application: 40/100 - Basic application was provided.
            - Sentiment: 40/100 - The candidate showed moderate confidence.

            **Average Performed Interview (Score: 60/100):**
            Question: "What is the purpose of using indexes in a database?"
            Answer: "Indexes are used to make searches faster in a database."
            Evaluation: The candidate correctly identifies the primary function of indexes but does not discuss other aspects, such as how they work, types of indexes, or their impact on database performance.
            Score Breakdown:
            - Accuracy: 60/100 - The response is accurate but lacks detail.
            - Coherence: 60/100 - The answer is clear and logical.
            - Technical Depth: 55/100 - Basic understanding demonstrated.
            - Application: 60/100 - Practical application was mentioned.
            - Sentiment: 65/100 - The candidate showed reasonable confidence.

            **Great Interview (Score: 80/100):**
            Question: "What are the key considerations when designing a dashboard for data visualization?"
            Answer: "The key considerations include understanding the target audience, ensuring data accuracy, choosing appropriate visual elements, and maintaining clarity. It’s also important to design for interactivity to allow users to drill down into the data."
            Evaluation: The candidate demonstrates a thorough understanding of data visualization principles and can articulate how to apply them in practical scenarios.
            Score Breakdown:
            - Accuracy: 80/100 - The answer is highly accurate and detailed.
            - Coherence: 75/100 - The response is well-structured and logical.
            - Technical Depth: 75/100 - The candidate demonstrates solid understanding.
            - Application: 80/100 - Practical applications were well explained.
            - Sentiment: 85/100 - The candidate appeared confident.

            **Excellent Interview (Score: 100/100):**
            Question: "Describe how you would optimize a query that is running too slowly in a large database."
            Answer: "I would start by analyzing the query execution plan to identify bottlenecks. Then, I would consider adding indexes, optimizing the query structure, and possibly partitioning the table to distribute the data more efficiently. If necessary, I would refactor the query to reduce complexity and improve performance."
            Evaluation: The candidate provides a comprehensive answer, demonstrating a deep understanding of query optimization techniques and practical steps to improve database performance.
            Score Breakdown:
            - Accuracy: 100/100 - The answer is detailed and correct.
            - Coherence: 95/100 - The response is well-structured and easy to follow.
            - Technical Depth: 100/100 - Exceptional understanding of the topic.
            - Application: 95/100 - Practical and effective solutions were provided.
            - Sentiment: 100/100 - The candidate appeared highly confident and knowledgeable.

            Combine the evaluations of each question to provide a final score for the entire interview by taking the average of each category.

            Do not show the topic of the question, do not show the key points, do not show the evaluation, and do not show the accuracy.
            Do not ask the same question.
            Do not repeat the question.

            Resume: 
            {context}
            
            Question: {question}
            Answer: """

        # software engineer
    swe_template = """
        I want you to act as an interviewer. Remember, you are the interviewer, not the candidate.

        Let’s think step by step.

        Based on the Resume, 
        Create a guideline with the following topics for an interview to test the knowledge of the candidate on necessary skills for being a Software Engineer.

        The questions should be in the context of the resume.

        There are 3 main topics: 
        1. Background and Skills 
        2. Work Experience
        3. Projects (if applicable)

        For each question:
            - Identify the topic and select relevant key points related to Software Engineering (e.g., algorithms, data structures, system design, coding languages).
            - Evaluate the candidate's response for accuracy, coherence, and technical depth, with a focus on problem-solving and coding efficiency.
            - Rate the accuracy on a scale of 0 to 100 based on how well the response matches the key points, especially in coding challenges.
            - Adjust the score based on the difficulty of the question, such as algorithm complexity or system architecture depth.
            - Increase or decrease the complexity of follow-up questions based on previous answers.
            - Include scenario-based questions to assess problem-solving in real-world contexts.
            - Analyze sentiment and confidence during the response.

        Here are some example evaluations:

        **Poorly Performed Interview (Score: 30/100):**
        Question: "What is a linked list?"
        Answer: "It's like a list of data."
        Evaluation: The answer is incomplete and lacks understanding of the structure and functionality of linked lists.
        Score Breakdown:
        - Accuracy: 30/100 - Basic concept was identified, but lacks depth.
        - Coherence: 35/100 - Response is too vague.
        - Technical Depth: 20/100 - Little understanding of linked lists.
        - Problem-Solving: 25/100 - The response shows weak problem-solving skills.
        - Sentiment: 30/100 - The candidate seemed unsure and hesitant.

        **Mediocre Performed Interview (Score: 40/100):**
        Question: "Explain the difference between a stack and a queue."
        Answer: "A stack is LIFO and a queue is FIFO."
        Evaluation: The candidate correctly identifies the basic differences but does not explain the use cases or operational details.
        Score Breakdown:
        - Accuracy: 40/100 - The answer is correct but lacks depth.
        - Coherence: 45/100 - The response is clear but too brief.
        - Technical Depth: 35/100 - Limited explanation provided.
        - Problem-Solving: 40/100 - Basic problem-solving approach demonstrated.
        - Sentiment: 40/100 - Moderate confidence in the response.

        **Average Performed Interview (Score: 60/100):**
        Question: "What is the purpose of using indexes in a database?"
        Answer: "Indexes are used to make searches faster in a database."
        Evaluation: The candidate correctly identifies the primary function of indexes but does not discuss other aspects, such as how they work, types of indexes, or their impact on database performance.
        Score Breakdown:
        - Accuracy: 60/100 - The response is accurate but lacks detail.
        - Coherence: 60/100 - The answer is clear and logical.
        - Technical Depth: 55/100 - Basic understanding demonstrated.
        - Problem-Solving: 60/100 - Practical application was mentioned.
        - Sentiment: 65/100 - The candidate showed reasonable confidence.

        **Great Interview (Score: 80/100):**
        Question: "What are the key considerations when designing a scalable system?"
        Answer: "The key considerations include understanding the system requirements, designing for scalability, ensuring data consistency, and choosing appropriate technology stacks. It’s also important to design for reliability and fault tolerance."
        Evaluation: The candidate demonstrates a thorough understanding of system design principles and can articulate how to apply them in practical scenarios.
        Score Breakdown:
        - Accuracy: 80/100 - The answer is highly accurate and detailed.
        - Coherence: 75/100 - The response is well-structured and logical.
        - Technical Depth: 75/100 - The candidate demonstrates solid understanding.
        - Problem-Solving: 80/100 - Practical applications were well explained.
        - Sentiment: 85/100 - The candidate appeared confident.

        **Excellent Interview (Score: 100/100):**
        Question: "Describe how you would design a scalable system to handle millions of transactions per second."
        Answer: "I would start by considering the architecture, such as microservices, distributed databases, and load balancing. I’d ensure fault tolerance, data consistency, and scalability by implementing techniques like sharding and replication."
        Evaluation: The candidate demonstrates a deep understanding of system design principles and can articulate a well-thought-out approach.
        Score Breakdown:
        - Accuracy: 100/100 - The answer is highly accurate and detailed.
        - Coherence: 95/100 - The response is well-structured and easy to follow.
        - Technical Depth: 100/100 - Exceptional understanding of the topic.
        - Problem-Solving: 95/100 - Practical and effective solutions were provided.
        - Sentiment: 100/100 - The candidate appeared highly confident and knowledgeable.

        Combine the evaluations of each question to provide a final score for the entire interview by taking the average of each category.

        Do not show the topic of the question, do not show the key points, do not show the evaluation, and do not show the accuracy.
        Do not ask the same question.
        Do not repeat the question.

        Resume: 
        {context}
        
        Question: {question}
        Answer: """

    marketing_template = """
        I want you to act as an interviewer. Remember, you are the interviewer, not the candidate.

        Let’s think step by step.

        Based on the Resume, 
        Create a guideline with the following topics for an interview to test the knowledge of the candidate on necessary skills for being a Marketing Associate.

        The questions should be in the context of the resume.

        There are 3 main topics: 
        1. Background and Skills 
        2. Work Experience
        3. Projects (if applicable)

        For each question:
            - Identify the topic and select relevant key points related to Marketing (e.g., campaign strategy, digital marketing tools, market analysis).
            - Evaluate the candidate's response for accuracy, coherence, and strategic depth, particularly in understanding market trends and consumer behavior.
            - Rate the accuracy on a scale of 0 to 100 based on how well the response aligns with key marketing principles.
            - Adjust the score based on the complexity of the question, such as the depth of analysis or creativity in campaign ideas.
            - Adjust the complexity of follow-up questions based on previous answers.
            - Include scenario-based questions to evaluate real-world applications.
            - Analyze sentiment and confidence during responses.

        Here are some example evaluations:

        **Score: 20/100**
        - **Question:** "What is a marketing funnel?"
        - **Answer:** "It's a way to get customers."
        - **Evaluation:** The answer is too vague and does not demonstrate an understanding of the marketing funnel concept. The candidate fails to mention the stages of the funnel or its purpose in guiding customers through the buying process.
        - **Score Breakdown:**
            - Accuracy: 20/100 - The response is technically correct but lacks detail.
            - Coherence: 30/100 - The response is clear but incomplete.
            - Strategic Depth: 10/100 - No depth or understanding shown.
            - Application: 20/100 - No practical application mentioned.
            - Sentiment: 20/100 - The candidate seemed uncertain.

        **Score: 40/100**
        - **Question:** "How do you measure the success of a marketing campaign?"
        - **Answer:** "I look at sales."
        - **Evaluation:** The candidate identifies a correct metric but does not mention other important metrics like ROI, customer engagement, or conversion rates. The answer lacks depth and fails to demonstrate a comprehensive understanding of campaign analysis.
        - **Score Breakdown:**
            - Accuracy: 40/100 - The answer is correct but incomplete.
            - Coherence: 45/100 - The response is clear but lacks depth.
            - Strategic Depth: 35/100 - Limited understanding of comprehensive metrics.
            - Application: 40/100 - Basic application mentioned.
            - Sentiment: 40/100 - Moderate confidence.

        **Score: 60/100**
        - **Question:** "What are the key components of a digital marketing strategy?"
        - **Answer:** "You need to use social media and email."
        - **Evaluation:** The candidate identifies some components of a digital marketing strategy but fails to mention others such as content marketing, SEO, and analytics. The response lacks a holistic view of the strategy.
        - **Score Breakdown:**
            - Accuracy: 60/100 - The response is accurate but lacks breadth.
            - Coherence: 60/100 - The answer is clear and logical.
            - Strategic Depth: 55/100 - Basic understanding demonstrated.
            - Application: 60/100 - Practical application was mentioned.
            - Sentiment: 65/100 - The candidate showed reasonable confidence.

        **Score: 80/100**
        - **Question:** "How would you approach creating a marketing campaign for a new product launch?"
        - **Answer:** "I would start by identifying the target audience, then develop key messages, choose the right channels, and set clear goals for the campaign. I would also plan for testing and optimization throughout the campaign."
        - **Evaluation:** The candidate demonstrates a solid understanding of how to plan and execute a marketing campaign. However, the answer could benefit from more specific examples or detailed strategies for each stage.
        - **Score Breakdown:**
            - Accuracy: 80/100 - The answer is highly accurate and well-explained.
            - Coherence: 75/100 - The response is well-structured and logical.
            - Strategic Depth: 75/100 - Strong understanding demonstrated.
            - Application: 80/100 - Practical application was well explained.
            - Sentiment: 85/100 - The candidate appeared confident.

        **Score: 100/100**
        - **Question:** "Explain how you would conduct a market analysis for a new product launch."
        - **Answer:** "I would start by identifying the target audience, analyzing competitors, and assessing market trends. I’d use tools like SWOT analysis and customer surveys to gather data and inform the strategy. Additionally, I would look at historical data and consumer behavior insights to refine the approach."
        - **Evaluation:** The candidate provides a comprehensive and detailed answer, demonstrating a deep understanding of market analysis and practical steps to implement it effectively.
        - **Score Breakdown:**
            - Accuracy: 100/100 - The answer is detailed and correct.
            - Coherence: 95/100 - The response is well-structured and easy to follow.
            - Strategic Depth: 100/100 - Exceptional understanding of the topic.
            - Application: 95/100 - Practical and effective solutions were provided.
            - Sentiment: 100/100 - The candidate appeared highly confident and knowledgeable.

        Combine the evaluations of each question to provide a final score for the entire interview by taking the average of each category.

        Do not show the topic of the question, do not show the key points, do not show the evaluation, and do not show the accuracy.
        Do not ask the same question.
        Do not repeat the question.

        Resume: 
        {context}
        
        Question: {question}
        Answer: """

    jd_template = """
        I want you to act as an interviewer. Remember, you are the interviewer, not the candidate.

        Let’s think step by step.

        Based on the job description, 
        Create a guideline with the following topics for an interview to test the technical knowledge of the candidate on necessary skills.

        For example:
        If the job description requires knowledge of data mining, GPT Interviewer will ask you questions like "Explain overfitting" or "How does backpropagation work?"
        If the job description requires knowledge of statistics, GPT Interviewer will ask you questions like "What is the difference between Type I and Type II error?"

        For each question:
            - Identify the topic and select relevant key points related to the job description (e.g., specific technical skills, tools, methodologies).
            - Evaluate the candidate's response for accuracy, coherence, and technical depth, particularly in how well they meet the job's requirements.
            - Rate the accuracy on a scale of 0 to 100 based on how well the response aligns with the job description.
            - Adjust the score based on the complexity of the job's requirements, such as advanced technical skills or specialized knowledge.
            - Adjust the complexity of follow-up questions based on previous answers.
            - Include scenario-based questions to assess real-world applications.
            - Analyze sentiment and confidence during the response.

        Here are some example evaluations:

        **Score: 20/100**
        - **Question:** "Explain what overfitting is."
        - **Answer:** "It's when the model is too fitted."
        - **Evaluation:** The answer is vague and lacks a clear explanation of overfitting or its implications in data modeling. The candidate fails to demonstrate an understanding of the concept or how to address it.
        - **Score Breakdown:**
            - Accuracy: 20/100 - The concept is identified but lacks depth.
            - Coherence: 30/100 - The response is vague.
            - Technical Depth: 20/100 - Little understanding of overfitting.
            - Application: 25/100 - No practical application mentioned.
            - Sentiment: 30/100 - The candidate appeared unsure.

        **Score: 40/100**
        - **Question:** "What is the difference between Type I and Type II errors?"
        - **Answer:** "Type I is a false positive, and Type II is a false negative."
        - **Evaluation:** The candidate provides a basic answer but does not elaborate on the implications or scenarios where these errors occur. The response lacks depth and practical examples.
        - **Score Breakdown:**
            - Accuracy: 40/100 - The basic concept is correct.
            - Coherence: 45/100 - The response is clear but lacks depth.
            - Technical Depth: 35/100 - Limited understanding shown.
            - Application: 40/100 - Basic application mentioned.
            - Sentiment: 40/100 - Moderate confidence.

        **Score: 60/100**
        - **Question:** "Can you explain the difference between supervised and unsupervised learning?"
        - **Answer:** "Supervised learning uses labeled data, and unsupervised learning does not."
        - **Evaluation:** The candidate correctly identifies the basic difference but does not go into details about when to use each type of learning or provide examples of algorithms used in both.
        - **Score Breakdown:**
            - Accuracy: 60/100 - The answer is accurate but lacks detail.
            - Coherence: 60/100 - The response is clear and logical.
            - Technical Depth: 55/100 - Basic understanding demonstrated.
            - Application: 60/100 - Practical application was mentioned.
            - Sentiment: 65/100 - The candidate showed reasonable confidence.

        **Score: 80/100**
        - **Question:** "Describe how you would handle a situation where your model shows signs of overfitting."
        - **Answer:** "I would use techniques like cross-validation, regularization, and increasing the training data to prevent overfitting. I'd also consider simplifying the model or using ensemble methods to enhance generalization."
        - **Evaluation:** The candidate provides a comprehensive answer, demonstrating a strong understanding of overfitting and practical methods to address it. However, more specific examples or details on the techniques would enhance the response.
        - **Score Breakdown:**
            - Accuracy: 80/100 - The answer is highly accurate and well-explained.
            - Coherence: 75/100 - The response is well-structured and logical.
            - Technical Depth: 75/100 - Strong understanding demonstrated.
            - Application: 80/100 - Practical application was well explained.
            - Sentiment: 85/100 - The candidate appeared confident.

        **Score: 100/100**
        - **Question:** "Explain how you would optimize a deep learning model to reduce training time without compromising accuracy."
        - **Answer:** "I would start by optimizing the dataset, such as reducing dimensionality or using data augmentation. I’d also experiment with model architecture adjustments, like using a smaller network or applying techniques like transfer learning. Additionally, I'd explore hardware optimizations like using GPUs or distributed computing."
        - **Evaluation:** The candidate provides a comprehensive and detailed answer, demonstrating a deep understanding of model optimization techniques and practical steps to implement them effectively.
        - **Score Breakdown:**
            - Accuracy: 100/100 - The answer is detailed and correct.
            - Coherence: 95/100 - The response is well-structured and easy to follow.
            - Technical Depth: 100/100 - Exceptional understanding of the topic.
            - Application: 95/100 - Practical and effective solutions were provided.
            - Sentiment: 100/100 - The candidate appeared highly confident and knowledgeable.

        Combine the evaluations of each question to provide a final score for the entire interview by taking the average of each category.

        Do not show the topic of the question, do not show the key points, do not show the evaluation, and do not show the accuracy.
        Do not ask the same question.
        Do not repeat the question.

        Job Description: 
        {context}
        
        Question: {question}
        Answer: """

    behavioral_template = """
        I want you to act as an interviewer. Remember, you are the interviewer, not the candidate.

        Let’s think step by step.

        Based on the keywords, 
        Create a guideline with the following topics for a behavioral interview to test the soft skills of the candidate.

        For each question:
            - Identify the topic and select relevant key points related to the behavioral competencies being tested (e.g., teamwork, leadership, problem-solving).
            - Evaluate the candidate's response for clarity, relevance, and emotional intelligence, particularly in how they handle hypothetical or past situations.
            - Rate the response on a scale of 0 to 100 based on how well it demonstrates the desired behavioral competencies.
            - Adjust the score based on the complexity of the situation or scenario described.
            - Adjust the complexity of follow-up questions based on previous answers.
            - Include scenario-based questions to evaluate real-world behavior.
            - Analyze sentiment and confidence during responses.

        Here are some example evaluations:

        **Score: 20/100**
        - **Question:** "Tell me about a time when you faced a conflict at work."
        - **Answer:** "I don't really remember any conflicts."
        - **Evaluation:** The candidate fails to provide a relevant example or demonstrate how they handle conflicts, leading to a low score in problem-solving and emotional intelligence.
        - **Score Breakdown:**
            - Clarity: 20/100 - The response lacks clarity.
            - Relevance: 25/100 - No relevant example provided.
            - Emotional Intelligence: 20/100 - No demonstration of emotional intelligence.
            - Problem-Solving: 25/100 - Poor problem-solving skills.
            - Sentiment: 30/100 - The candidate appeared uncertain.

        **Score: 40/100**
        - **Question:** "Describe a situation where you had to work under pressure."
        - **Answer:** "I worked late to finish a project. It was stressful, but I managed."
        - **Evaluation:** The candidate gives a basic response but lacks details on how they managed the pressure or the outcome of the situation. The answer is incomplete and lacks depth in demonstrating stress management skills.
        - **Score Breakdown:**
            - Clarity: 40/100 - The response is clear but lacks detail.
            - Relevance: 45/100 - The example is relevant but lacks depth.
            - Emotional Intelligence: 35/100 - Limited demonstration of emotional intelligence.
            - Problem-Solving: 40/100 - Basic problem-solving skills.
            - Sentiment: 40/100 - The candidate showed moderate confidence.

        **Score: 60/100**
        - **Question:** "Can you give an example of how you handled a challenging project?"
        - **Answer:** "I had to manage a project with a tight deadline. I stayed organized and focused on completing tasks on time."
        - **Evaluation:** The candidate provides a relevant example but does not go into sufficient detail about the challenges faced or how they were overcome. The answer lacks depth in problem-solving and leadership skills.
        - **Score Breakdown:**
            - Clarity: 60/100 - The response is clear and logical.
            - Relevance: 60/100 - The example is relevant but lacks depth.
            - Emotional Intelligence: 55/100 - Basic understanding demonstrated.
            - Problem-Solving: 60/100 - Practical problem-solving mentioned.
            - Sentiment: 65/100 - The candidate showed reasonable confidence.

        **Score: 80/100**
        - **Question:** "Tell me about a time when you had to lead a team under difficult circumstances."
        - **Answer:** "During a critical project, one of our key team members fell ill. I had to redistribute the tasks and motivate the team to meet the deadline. I ensured open communication and supported the team through regular check-ins."
        - **Evaluation:** The candidate demonstrates solid leadership skills and an ability to manage a team under pressure. The response could benefit from more specific examples or outcomes of the leadership efforts.
        - **Score Breakdown:**
            - Clarity: 80/100 - The response is well-structured and logical.
            - Relevance: 75/100 - The example is relevant and well-explained.
            - Emotional Intelligence: 75/100 - Strong understanding demonstrated.
            - Problem-Solving: 80/100 - Effective problem-solving approach demonstrated.
            - Sentiment: 85/100 - The candidate appeared confident and empathetic.

        **Score: 100/100**
        - **Question:** "Describe a situation where you had to navigate a difficult decision with significant impact."
        - **Answer:** "I was leading a project that was running over budget. I had to decide whether to cut certain features or request additional funding. I conducted a thorough cost-benefit analysis, consulted with stakeholders, and ultimately decided to cut non-essential features while ensuring the project's core objectives were met. The decision was well-received, and the project was completed successfully within the revised budget."
        - **Evaluation:** The candidate provides a detailed and well-thought-out example, demonstrating strong decision-making, problem-solving, and leadership skills. The response is clear, relevant, and shows a high level of emotional intelligence and confidence.
        - **Score Breakdown:**
            - Clarity: 100/100 - The response is detailed and clear.
            - Relevance: 95/100 - The example is highly relevant and well-chosen.
            - Emotional Intelligence: 100/100 - Exceptional demonstration of emotional intelligence.
            - Problem-Solving: 95/100 - Strong and effective problem-solving approach.
            - Sentiment: 100/100 - The candidate appeared highly confident and knowledgeable.

        Combine the evaluations of each question to provide a final score for the entire interview.

        Do not show the topic of the question, do not show the key points, do not show the evaluation, and do not show the accuracy.
        Do not ask the same question.
        Do not repeat the question.

        Keywords: 
        {context}
        
        Question: {question}
        Answer: """

    feedback_template = """
        Based on the chat history, I would like you to evaluate the candidate based on the following format:

        Summarization: Summarize the conversation in a short paragraph.

        Pros: Give positive feedback to the candidate.

        Cons: Tell the candidate what they can improve on.

        Scoring Breakdown:
            - Accuracy: Explain how accurate the candidate’s responses were, and provide a score out of 100. Justify the score with examples from their answers.
            - Coherence: Evaluate the logical flow and clarity of the candidate's responses. Provide a score out of 100 and explain your reasoning.
            - Technical Depth: Assess the depth of the candidate's technical knowledge and provide a score out of 100. Include specific examples to support the score.
            - Problem-Solving: Rate how effectively the candidate solved problems or handled scenarios. Provide a score out of 100 and explain your reasoning.
            - Application: Assess how well the candidate applied their knowledge to practical scenarios. Provide a score out of 100 and explain your reasoning.
            - Sentiment: Analyze the candidate's confidence and emotional tone throughout the interview. Provide a score out of 100 with an explanation.

        Score: Combine the scores from the content evaluation, signal processing, and sentiment analysis to provide an overall score out of 100 by taking the average of each category. The final score is a holistic measure of accuracy, coherence, depth, problem-solving, application, and confidence. Explain how the final score was derived, taking into account both the content and delivery of the responses. 

        Sample Answers: Provide sample answers to each of the questions in the interview guideline.

        Remember, the candidate has no idea what the interview guideline is. Sometimes the candidate may not even answer the question.

        Current conversation:
        {history}

        Interviewer: {input}
        Response: """

########################################################################################
# Prompt Selector

from langchain.prompts import PromptTemplate

def prompt_selector(position: str, prompts: classmethod) -> dict:

    """ Select the prompt template based on the position """

    # PROMPT = PromptTemplate(
    #     template = prompts.position_template, input_variables=["context", "question"]
    # )
    # chain_type_kwargs = {"prompt": PROMPT}

    if position == 'Data Analyst':
        PROMPT = PromptTemplate(
            template= prompts.da_template, input_variables=["context", "question"]
        )
        chain_type_kwargs = {"prompt": PROMPT}

    if position == 'Software Engineer':
        PROMPT = PromptTemplate(
            template= prompts.swe_template, input_variables=["context", "question"]
        )
        chain_type_kwargs = {"prompt": PROMPT}

    if position == 'Marketing':
        PROMPT = PromptTemplate(
            template= prompts.marketing_template, input_variables=["context", "question"]
        )
        chain_type_kwargs = {"prompt": PROMPT}

    return chain_type_kwargs

########################################################################################
# Streamlit Audio Recording

import os
import numpy as np
import streamlit as st
from io import BytesIO
import streamlit.components.v1 as components

def st_audiorec():

    # get parent directory relative to current directory
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    # Custom REACT-based component for recording client audio in browser
    build_dir = os.path.join(parent_dir, "frontend/build")
    # specify directory and initialize st_audiorec object functionality
    st_audiorec = components.declare_component("st_audiorec", path=build_dir)

    # Create an instance of the component: STREAMLIT AUDIO RECORDER
    raw_audio_data = st_audiorec()  # raw_audio_data: stores all the data returned from the streamlit frontend
    wav_bytes = None                # wav_bytes: contains the recorded audio in .WAV format after conversion

    # the frontend returns raw audio data in the form of arraybuffer
    # (this arraybuffer is derived from web-media API WAV-blob data)

    if isinstance(raw_audio_data, dict):  # retrieve audio data
        with st.spinner('retrieving audio-recording...'):
            ind, raw_audio_data = zip(*raw_audio_data['arr'].items())
            ind = np.array(ind, dtype=int)  # convert to np array
            raw_audio_data = np.array(raw_audio_data)  # convert to np array
            sorted_ints = raw_audio_data[ind]
            stream = BytesIO(b"".join([int(v).to_bytes(1, "big") for v in sorted_ints]))
            # wav_bytes contains audio data in byte format, ready to be processed further
            wav_bytes = stream.read()

    return wav_bytes

########################################################################################
# Synthesize Speech

import streamlit as st
import os
from tempfile import gettempdir

def synthesize_speech(text, service):
    if service == "amazon":
        import sys
        import subprocess
        from contextlib import closing
        import boto3
        
        Session = boto3.Session(
        aws_access_key_id = "AKIA5FTZCRWWE7V4QPG2",
        aws_secret_access_key = "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",
        region_name = "us-east-1")

        Polly = Session.client("polly")
        response = Polly.synthesize_speech(
            Text=text,
            OutputFormat="mp3",
            VoiceId="Joanna")
        if "AudioStream" in response:
            # Note: Closing the stream is important because the service throttles on the
            # number of parallel connections. Here we are using contextlib.closing to
            # ensure the close method of the stream object will be called automatically
            # at the end of the with statement's scope.
            with closing(response["AudioStream"]) as stream:
                output = os.path.join(gettempdir(), "speech.mp3")

                try:
                    # Open a file for writing the output as a binary stream
                    with open(output, "wb") as file:
                        file.write(stream.read())
                except IOError as error:
                    # Could not write to file, exit gracefully
                    print(error)
                    sys.exit(-1)
        else:
            # The response didn't contain audio data, exit gracefully
            print("Could not stream audio")
            sys.exit(-1)

        # Play the audio using the platform's default player
        if sys.platform == "win32":
            os.startfile(output)
        else:
            # The following works on macOS and Linux. (Darwin = mac, xdg-open = linux).
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, output])
    
    elif service == "google":
        from gtts import gTTS

        tts = gTTS(text=text, lang='en')
        output = os.path.join(gettempdir(), "speech.mp3")
        tts.save(output)

        # Play the audio using the platform's default player
        st.audio(output, format="audio/mp3", autoplay=True)

    elif service == "openai":
        from openai import OpenAI
        from dotenv import load_dotenv
        OpenAI.api_key = os.getenv("OPENAI_API_KEY")

        load_dotenv()

        client = OpenAI()
        response = client.audio.speech.create(model="tts-1",voice="echo",input=text)
        output = os.path.join(gettempdir(), "speech.mp3")
        response.stream_to_file(output)

        # Play the audio using the platform's default player
        st.audio(output, format="audio/mp3", autoplay=True)

    return output

########################################################################################
# Speech Recognition

from openai import OpenAI
import assemblyai as aai
import os
from dotenv import load_dotenv
load_dotenv()
import wave

OpenAI.api_key = os.getenv("OPENAI_API_KEY")
aai.settings.api_key = os.getenv("ASSEMBLYAI_API_KEY")

class Config:
    channels = 2
    sample_width = 2
    sample_rate = 44100

def save_wav_file(file_path, wav_bytes):
    with wave.open(file_path, 'wb') as wav_file:
        wav_file.setnchannels(Config.channels)
        wav_file.setsampwidth(Config.sample_width)
        wav_file.setframerate(Config.sample_rate)
        wav_file.writeframes(wav_bytes)

def transcribe(file_path):
    # client = OpenAI()
    # audio_file= open(file_path, "rb")
    # transcription = client.audio.transcriptions.create(
    # model="whisper-1", 
    # file=audio_file
    # )

    transcriber = aai.Transcriber()
    transcription = transcriber.transcribe(file_path)

    return transcription.text

# print(transcribe("audio.wav"))

########################################################################################
# Initialize Session State

import streamlit as st
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import NLTKTextSplitter
from langchain.memory import ConversationBufferMemory
from langchain.chains import RetrievalQA, ConversationChain
# from prompts.prompts import templates
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from PyPDF2 import PdfReader
# from prompts.prompt_selector import prompt_selector

def embedding(text):
    """embeddings"""
    text_splitter = NLTKTextSplitter()
    texts = text_splitter.split_text(text)
     # Create emebeddings
    embeddings = OpenAIEmbeddings()
    docsearch = FAISS.from_texts(texts, embeddings)
    return docsearch

def resume_reader(resume):
    pdf_reader = PdfReader(resume)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def initialize_session_state(template = None, position = None):
    """ initialize session states """
    if 'jd' in st.session_state:
        st.session_state.docsearch = embedding(st.session_state.jd)
    else:
        st.session_state.docsearch = embedding(resume_reader(st.session_state.resume))

    #if 'retriever' not in st.session_state:
    st.session_state.retriever = st.session_state.docsearch.as_retriever(search_type="similarity")
    #if 'chain_type_kwargs' not in st.session_state:
    if 'jd' in st.session_state:
        Interview_Prompt = PromptTemplate(input_variables=["context", "question"],
                                              template=template)
        st.session_state.chain_type_kwargs = {"prompt": Interview_Prompt}
    else:
            st.session_state.chain_type_kwargs = prompt_selector(position, templates)
    #if 'memory' not in st.session_state:
    st.session_state.memory = ConversationBufferMemory()
    # interview history
    #if "history" not in st.session_state:
    st.session_state.history = []
    # token count
    #if "token_count" not in st.session_state:
    st.session_state.token_count = 0
    #if "guideline" not in st.session_state:
    llm = ChatOpenAI(
            model_name="gpt-3.5-turbo",
            temperature=0.6, )
    st.session_state.guideline = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type_kwargs=st.session_state.chain_type_kwargs, chain_type='stuff',
            retriever=st.session_state.retriever, memory=st.session_state.memory).run(
            "Create an interview guideline and prepare only one questions for each topic. Make sure the questions tests the technical knowledge")
    # llm chain and memory
    #if "screen" not in st.session_state:
    llm = ChatOpenAI(
            model_name="gpt-3.5-turbo",
            temperature=0.8, )
    PROMPT = PromptTemplate(
            input_variables=["history", "input"],
            template="""I want you to act as an interviewer strictly following the guideline in the current conversation.

                            Ask me questions and wait for my answers like a real person.
                            Do not write explanations.
                            Ask question like a real person, only one question at a time.
                            Do not ask the same question.
                            Do not repeat the question.
                            Do ask follow-up questions if necessary. 
                            You name is AIInterviewer.
                            I want you to only reply as an interviewer.
                            Do not write all the conversation at once.
                            If there is an error, point it out.

                            Current Conversation:
                            {history}

                            Candidate: {input}
                            AI: """)
    st.session_state.screen = ConversationChain(prompt=PROMPT, llm=llm,
                                                    memory=st.session_state.memory)
    #if "feedback" not in st.session_state:
    llm = ChatOpenAI(
        model_name = "gpt-3.5-turbo",
        temperature = 0.5,)
    st.session_state.feedback = ConversationChain(
            prompt=PromptTemplate(input_variables = ["history", "input"], template = templates.feedback_template),
            llm=llm,
            memory = st.session_state.memory,
        )
########################################################################################
# Streamlit ResumeScreenPage Setup

def ResumeScreenPage():
    import streamlit as st
    from streamlit_lottie import st_lottie
    from typing import Literal
    from dataclasses import dataclass
    import json
    # import base64
    from langchain.memory import ConversationBufferMemory
    from langchain_community.callbacks import get_openai_callback
    from langchain_openai import ChatOpenAI
    from langchain.chains import ConversationChain, RetrievalQA
    from langchain.prompts.prompt import PromptTemplate
    from langchain.text_splitter import NLTKTextSplitter
    from langchain_community.embeddings import OpenAIEmbeddings
    from langchain_community.vectorstores import FAISS
    import nltk
    # from prompts.prompts import templates
    # Audio
    # from speech_recognition.openai_whisper import save_wav_file, transcribe
    from audio_recorder_streamlit import audio_recorder
    # from aws.synthesize_speech3 import synthesize_speech
    from IPython.display import Audio
    from openai import OpenAI
    import os
    from dotenv import load_dotenv
    load_dotenv()
    OpenAI.api_key = os.getenv("OPENAI_API_KEY")
    nltk.download('punkt')

    def load_lottiefile(filepath: str):
        with open(filepath, "r") as f:
            return json.load(f)
    st_lottie(load_lottiefile("images/welcome.json"), speed=1, reverse=False, loop=True, quality="high", height=300)

    #st.markdown("""solutions to potential errors:""")
    with st.expander("""Why did I encounter errors when I tried to talk to the AI Interviewer?"""):
        st.write("""This is because the app failed to record. Make sure that your microphone is connected and that you have given permission to the browser to access your microphone.""")
    with st.expander("""Why did I encounter errors when I tried to upload my resume?"""):
        st.write("""
        Please make sure your resume is in pdf format. More formats will be supported in the future.
        """)

    st.markdown("""\n""")
    position = st.selectbox("Select the position you are applying for", ["Data Analyst", "Software Engineer", "Marketing"])
    resume = st.file_uploader("Upload your resume", type=["pdf"])
    auto_play = st.checkbox("Let AI interviewer speak! (Please don't switch during the interview)")

    #st.toast("4097 tokens is roughly equivalent to around 800 to 1000 words or 3 minutes of speech. Please keep your answer within this limit.")

    @dataclass
    class Message:
        """Class for keeping track of interview history."""
        origin: Literal["human", "ai"]
        message: str

    def save_vector(resume):
        """embeddings"""
        nltk.download('punkt')
        pdf_reader = PdfReader(resume)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        # Split the document into chunks
        text_splitter = NLTKTextSplitter()
        texts = text_splitter.split_text(text)

        embeddings = OpenAIEmbeddings()
        docsearch = FAISS.from_texts(texts, embeddings)
        return docsearch

    def initialize_session_state_resume():
        # convert resume to embeddings
        if 'docsearch' not in st.session_state:
            st.session_state.docserch = save_vector(resume)
        # retriever for resume screen
        if 'retriever' not in st.session_state:
            st.session_state.retriever = st.session_state.docserch.as_retriever(search_type="similarity")
        # prompt for retrieving information
        if 'chain_type_kwargs' not in st.session_state:
            st.session_state.chain_type_kwargs = prompt_selector(position, templates)
        # interview history
        if "resume_history" not in st.session_state:
            st.session_state.resume_history = []
            st.session_state.resume_history.append(Message(origin="ai", message="Hello, I am your interivewer today. I will ask you some questions regarding your resume and your experience. Please start by saying hello or introducing yourself. Note: The maximum length of your answer is 4097 tokens!"))
        # token count
        if "token_count" not in st.session_state:
            st.session_state.token_count = 0
        # memory buffer for resume screen
        if "resume_memory" not in st.session_state:
            st.session_state.resume_memory = ConversationBufferMemory(human_prefix = "Candidate: ", ai_prefix = "Interviewer")
        # guideline for resume screen
        if "resume_guideline" not in st.session_state:
            llm = ChatOpenAI(
            model_name = "gpt-3.5-turbo",
            temperature = 0.5,)

            st.session_state.resume_guideline = RetrievalQA.from_chain_type(
                llm=llm,
                chain_type_kwargs=st.session_state.chain_type_kwargs, chain_type='stuff',
                retriever=st.session_state.retriever, memory = st.session_state.resume_memory).run("Create an interview guideline and prepare only two questions for each topic. Make sure the questions tests the knowledge")
        # llm chain for resume screen
        if "resume_screen" not in st.session_state:
            llm = ChatOpenAI(
                model_name="gpt-3.5-turbo",
                temperature=0.7, )

            PROMPT = PromptTemplate(
                input_variables=["history", "input"],
                template= """I want you to act as an interviewer strictly following the guideline in the current conversation.
                
                Ask me questions and wait for my answers like a human. Do not write explanations.
                Candidate has no assess to the guideline.
                Only ask one question at a time. 
                Do ask follow-up questions if you think it's necessary.
                Do not ask the same question.
                Do not repeat the question.
                Candidate has no assess to the guideline.
                You name is GPTInterviewer.
                I want you to only reply as an interviewer.
                Do not write all the conversation at once.
                Candiate has no assess to the guideline.
                
                Current Conversation:
                {history}
                
                Candidate: {input}
                AI: """)
            st.session_state.resume_screen =  ConversationChain(prompt=PROMPT, llm = llm, memory = st.session_state.resume_memory)
        # llm chain for generating feedback
        if "resume_feedback" not in st.session_state:
            llm = ChatOpenAI(
                model_name="gpt-3.5-turbo",
                temperature=0.5,)
            st.session_state.resume_feedback = ConversationChain(
                prompt=PromptTemplate(input_variables=["history","input"], template=templates.feedback_template),
                llm=llm,
                memory=st.session_state.resume_memory,
            )

    def answer_call_back():
        with get_openai_callback() as cb:
            human_answer = st.session_state.answer
            if voice:
                save_wav_file("temp/audio.wav", human_answer)
                try:
                    input = transcribe("temp/audio.wav")
                    # save human_answer to history
                except:
                    st.session_state.resume_history.append(Message("ai", "Sorry, I didn't get that."))
                    return "Please try again."
            else:
                input = human_answer
            st.session_state.resume_history.append(
                Message("human", input)
            )
            # OpenAI answer and save to history
            llm_answer = st.session_state.resume_screen.run(input)
            # speech synthesis and speak out
            audio_file_path = synthesize_speech(llm_answer, "openai")
            # create audio widget with autoplay
            audio_widget = Audio(audio_file_path, autoplay=True)
            # save audio data to history
            st.session_state.resume_history.append(
                Message("ai", llm_answer)
            )
            st.session_state.token_count += cb.total_tokens
            return audio_widget

    if position and resume:
        # intialize session state
        initialize_session_state_resume()
        credit_card_placeholder = st.empty()
        col1, col2 = st.columns(2)
        with col1:
            feedback = st.button("Get Interview Feedback")
        with col2:
            guideline = st.button("Show me interview guideline!")
        chat_placeholder = st.container()
        answer_placeholder = st.container()
        audio = None
        # if submit email adress, get interview feedback imediately
        if guideline:
            st.markdown(st.session_state.resume_guideline)
        if feedback:
            evaluation = st.session_state.resume_feedback.run("please give evalution regarding the interview")
            st.markdown(evaluation)
            st.download_button(label="Download Interview Feedback", data=evaluation, file_name="interview_feedback.txt")
            st.stop()
        else:
            with answer_placeholder:
                voice: bool = st.checkbox("I would like to speak with AI Interviewer!")
                if voice:
                    answer = audio_recorder(pause_threshold=2, sample_rate=44100)
                    #st.warning("An UnboundLocalError will occur if the microphone fails to record.")
                else:
                    answer = st.chat_input("Your answer")
                if answer:
                    st.session_state['answer'] = answer
                    audio = answer_call_back()

            with chat_placeholder:
                for answer in st.session_state.resume_history:
                    if answer.origin == 'ai':
                        if auto_play and audio:
                            with st.chat_message("assistant"):
                                st.write(answer.message)
                                st.write(audio)
                        else:
                            with st.chat_message("assistant"):
                                st.write(answer.message)
                    else:
                        with st.chat_message("user"):
                            st.write(answer.message)

            credit_card_placeholder.caption(f"""
                            Progress: {int(len(st.session_state.resume_history) / 30 * 100)}% completed.""")

########################################################################################
# Streamlit BehavioralScreenPage Setup

def BehavioralScreenPage():
    import streamlit as st
    from streamlit_lottie import st_lottie
    from typing import Literal
    from dataclasses import dataclass
    import json
    import base64
    from langchain.memory import ConversationBufferMemory
    from langchain_community.callbacks import get_openai_callback
    from langchain_openai import ChatOpenAI
    from langchain.chains import ConversationChain, RetrievalQA
    from langchain.prompts.prompt import PromptTemplate
    from langchain.text_splitter import NLTKTextSplitter
    from langchain_community.embeddings import OpenAIEmbeddings
    from langchain_community.vectorstores import FAISS
    import nltk
    # from prompts.prompts import templates
    # Audio
    # from speech_recognition.openai_whisper import save_wav_file, transcribe
    from audio_recorder_streamlit import audio_recorder
    # from aws.synthesize_speech3 import synthesize_speech
    from IPython.display import Audio
    from openai import OpenAI
    import os
    from dotenv import load_dotenv
    load_dotenv()
    OpenAI.api_key = os.getenv("OPENAI_API_KEY")
    nltk.download('punkt')

    def load_lottiefile(filepath: str):

        '''Load lottie animation file'''

        with open(filepath, "r") as f:
            return json.load(f)

    st_lottie(load_lottiefile("images/welcome.json"), speed=1, reverse=False, loop=True, quality="high", height=300)

    #st.markdown("""solutions to potential errors:""")
    with st.expander("""Why did I encounter errors when I tried to talk to the AI Interviewer?"""):
        st.write("""
        This is because the app failed to record. Make sure that your microphone is connected and that you have given permission to the browser to access your microphone.""")

    st.markdown("""\n""")
    jd = st.text_area("""Please enter the job description here (If you don't have one, enter keywords, such as "communication" or "teamwork" instead): """)
    auto_play = st.checkbox("Let AI interviewer speak! (Please don't switch during the interview)")
    #st.toast("4097 tokens is roughly equivalent to around 800 to 1000 words or 3 minutes of speech. Please keep your answer within this limit.")

    @dataclass
    class Message:
        '''dataclass for keeping track of the messages'''
        origin: Literal["human", "ai"]
        message: str

    def autoplay_audio(file_path: str):
        '''Play audio automatically'''
        def update_audio():
            global global_audio_md
            with open(file_path, "rb") as f:
                data = f.read()
                b64 = base64.b64encode(data).decode()
                global_audio_md = f"""
                    <audio controls autoplay="true">
                    <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                    </audio>
                    """
        def update_markdown(audio_md):
            st.markdown(audio_md, unsafe_allow_html=True)
        update_audio()
        update_markdown(global_audio_md)

    def embeddings(text: str):

        '''Create embeddings for the job description'''

        # nltk.download('punkt')
        text_splitter = NLTKTextSplitter()
        texts = text_splitter.split_text(text)
        # Create emebeddings
        embeddings = OpenAIEmbeddings()
        docsearch = FAISS.from_texts(texts, embeddings)
        retriever = docsearch.as_retriever(search_tupe='similarity search')
        return retriever

    def initialize_session_state():

        '''Initialize session state variables'''

        if "retriever" not in st.session_state:
            st.session_state.retriever = embeddings(jd)
        if "chain_type_kwargs" not in st.session_state:
            Behavioral_Prompt = PromptTemplate(input_variables=["context", "question"],
                                            template=templates.behavioral_template)
            st.session_state.chain_type_kwargs = {"prompt": Behavioral_Prompt}
        # interview history
        if "history" not in st.session_state:
            st.session_state.history = []
            st.session_state.history.append(Message("ai", "Hello there! I am your interviewer today. I will access your soft skills through a series of questions. Let's get started! Please start by saying hello or introducing yourself. Note: The maximum length of your answer is 4097 tokens!"))
        # token count
        if "token_count" not in st.session_state:
            st.session_state.token_count = 0
        if "memory" not in st.session_state:
            st.session_state.memory = ConversationBufferMemory()
        if "guideline" not in st.session_state:
            llm = ChatOpenAI(
                model_name="gpt-3.5-turbo",
                temperature=0.8, )
            st.session_state.guideline = RetrievalQA.from_chain_type(
                llm=llm,
                chain_type_kwargs=st.session_state.chain_type_kwargs, chain_type='stuff',
                retriever=st.session_state.retriever, memory=st.session_state.memory).run(
                "Create an interview guideline and prepare total of 8 questions. Make sure the questions tests the soft skills")
        # llm chain and memory
        if "conversation" not in st.session_state:
            llm = ChatOpenAI(
            model_name = "gpt-3.5-turbo",
            temperature = 0.8,)
            PROMPT = PromptTemplate(
                input_variables=["history", "input"],
                template="""I want you to act as an interviewer strictly following the guideline in the current conversation.
                                Candidate has no idea what the guideline is.
                                Ask me questions and wait for my answers. Do not write explanations.
                                Ask question like a real person, only one question at a time.
                                Do not ask the same question.
                                Do not repeat the question.
                                Do ask follow-up questions if necessary. 
                                You name is GPTInterviewer.
                                I want you to only reply as an interviewer.
                                Do not write all the conversation at once.
                                If there is an error, point it out.

                                Current Conversation:
                                {history}

                                Candidate: {input}
                                AI: """)
            st.session_state.conversation = ConversationChain(prompt=PROMPT, llm=llm,
                                                        memory=st.session_state.memory)
        if "feedback" not in st.session_state:
            llm = ChatOpenAI(
            model_name = "gpt-3.5-turbo",
            temperature = 0.5,)
            st.session_state.feedback = ConversationChain(
                prompt=PromptTemplate(input_variables = ["history", "input"], template = templates.feedback_template),
                llm=llm,
                memory = st.session_state.memory,
            )

    def answer_call_back():

        '''callback function for answering user input'''

        with get_openai_callback() as cb:
            # user input
            human_answer = st.session_state.answer
            # transcribe audio
            if voice:
                save_wav_file("temp/audio.wav", human_answer)
                try:
                    input = transcribe("temp/audio.wav")
                    # save human_answer to history
                except:
                    st.session_state.history.append(Message("ai", "Sorry, I didn't get that."))
                    return "Please try again."
            else:
                input = human_answer

            st.session_state.history.append(
                Message("human", input)
            )
            # OpenAI answer and save to history
            llm_answer = st.session_state.conversation.run(input)
            # speech synthesis and speak out
            audio_file_path = synthesize_speech(llm_answer, "openai")
            # create audio widget with autoplay
            audio_widget = Audio(audio_file_path, autoplay=True)
            # save audio data to history
            st.session_state.history.append(
                Message("ai", llm_answer)
            )
            st.session_state.token_count += cb.total_tokens
            return audio_widget

    ### ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
    if jd:

        initialize_session_state()
        credit_card_placeholder = st.empty()
        col1, col2 = st.columns(2)
        with col1:
            feedback = st.button("Get Interview Feedback")
        with col2:
            guideline = st.button("Show me interview guideline!")
        audio = None
        chat_placeholder = st.container()
        answer_placeholder = st.container()

        if guideline:
            st.write(st.session_state.guideline)
        if feedback:
            evaluation = st.session_state.feedback.run("please give evalution regarding the interview")
            st.markdown(evaluation)
            st.download_button(label="Download Interview Feedback", data=evaluation, file_name="interview_feedback.txt")
            st.stop()
        else:
            with answer_placeholder:
                voice: bool = st.checkbox("I would like to speak with AI Interviewer!")
                if voice:
                    answer = audio_recorder(pause_threshold=2.5, sample_rate=44100)
                    #st.warning("An UnboundLocalError will occur if the microphone fails to record.")
                else:
                    answer = st.chat_input("Your answer")
                if answer:
                    st.session_state['answer'] = answer
                    audio = answer_call_back()
            with chat_placeholder:
                for answer in st.session_state.history:
                    if answer.origin == 'ai':
                        if auto_play and audio:
                            with st.chat_message("assistant"):
                                st.write(answer.message)
                                st.write(audio)
                        else:
                            with st.chat_message("assistant"):
                                st.write(answer.message)
                    else:
                        with st.chat_message("user"):
                            st.write(answer.message)

            credit_card_placeholder.caption(f"""
                            Progress: {int(len(st.session_state.history) / 30 * 100)}% completed.
            """)

    else:
        st.info("Please submit job description to start interview.")

########################################################################################
# Streamlit ProfessionalScreenPage Setup

def TechnicalScreenPage():
    import streamlit as st
    from streamlit_lottie import st_lottie
    from typing import Literal
    from dataclasses import dataclass
    import json
    # import base64
    from langchain.memory import ConversationBufferMemory
    from langchain_community.callbacks import get_openai_callback
    from langchain_openai import ChatOpenAI
    from langchain.chains import ConversationChain, RetrievalQA
    from langchain.prompts.prompt import PromptTemplate
    from langchain.text_splitter import NLTKTextSplitter
    from langchain_community.embeddings import OpenAIEmbeddings
    from langchain_community.vectorstores import FAISS
    import nltk
    # from prompts.prompts import templates
    # Audio
    # from speech_recognition.openai_whisper import save_wav_file, transcribe
    from audio_recorder_streamlit import audio_recorder
    # from aws.synthesize_speech3 import synthesize_speech
    from IPython.display import Audio
    from openai import OpenAI
    import os
    from dotenv import load_dotenv
    load_dotenv()
    OpenAI.api_key = os.getenv("OPENAI_API_KEY")
    nltk.download('punkt')

    # Loads the "Welcome" animation
    def load_lottiefile(filepath: str):
        with open(filepath, "r") as f:
            return json.load(f)
        
    st_lottie(load_lottiefile("images/welcome.json"), speed=1, reverse=False, loop=True, quality="high", height=300)
    jd = st.text_area("Please enter the job description here (If you don't have one, enter keywords, such as PostgreSQL or Python instead): ")
    auto_play = st.checkbox("Let AI interviewer speak! (Please don't switch during the interview)")
    #st.toast("4097 tokens is roughly equivalent to around 800 to 1000 words or 3 minutes of speech. Please keep your answer within this limit.")

    @dataclass
    class Message:
        """class for keeping track of interview history."""
        origin: Literal["human", "ai"]
        message: str

    def save_vector(text):
        """embeddings"""

        text_splitter = NLTKTextSplitter()
        texts = text_splitter.split_text(text)
        # Create emebeddings
        embeddings = OpenAIEmbeddings()
        docsearch = FAISS.from_texts(texts, embeddings)
        return docsearch

    def initialize_session_state_jd():
        """ initialize session states """
        if 'jd_docsearch' not in st.session_state:
            st.session_state.jd_docserch = save_vector(jd)
        if 'jd_retriever' not in st.session_state:
            st.session_state.jd_retriever = st.session_state.jd_docserch.as_retriever(search_type="similarity")
        if 'jd_chain_type_kwargs' not in st.session_state:
            Interview_Prompt = PromptTemplate(input_variables=["context", "question"],
                                            template=templates.jd_template)
            st.session_state.jd_chain_type_kwargs = {"prompt": Interview_Prompt}
        if 'jd_memory' not in st.session_state:
            st.session_state.jd_memory = ConversationBufferMemory()
        # interview history
        if "jd_history" not in st.session_state:
            st.session_state.jd_history = []
            st.session_state.jd_history.append(Message("ai",
                                                    "Hello, Welcome to the interview. I am your interviewer today. I will ask you professional questions regarding the job description you submitted."
                                                    "Please start by introducting a little bit about yourself. Note: The maximum length of your answer is 4097 tokens!"))
        # token count
        if "token_count" not in st.session_state:
            st.session_state.token_count = 0
        if "jd_guideline" not in st.session_state:
            llm = ChatOpenAI(
            model_name = "gpt-3.5-turbo",
            temperature = 0.8,)
            st.session_state.jd_guideline = RetrievalQA.from_chain_type(
                llm=llm,
                chain_type_kwargs=st.session_state.jd_chain_type_kwargs, chain_type='stuff',
                retriever=st.session_state.jd_retriever, memory = st.session_state.jd_memory).run("Create an interview guideline and prepare only one questions for each topic. Make sure the questions tests the technical knowledge")
        # llm chain and memory
        if "jd_screen" not in st.session_state:
            llm = ChatOpenAI(
                model_name="gpt-3.5-turbo",
                temperature=0.8, )
            PROMPT = PromptTemplate(
                input_variables=["history", "input"],
                template="""I want you to act as an interviewer strictly following the guideline in the current conversation.
                                Candidate has no idea what the guideline is.
                                Ask me questions and wait for my answers. Do not write explanations.
                                Ask question like a real person, only one question at a time.
                                Do not ask the same question.
                                Do not repeat the question.
                                Do ask follow-up questions if necessary. 
                                You name is GPTInterviewer.
                                I want you to only reply as an interviewer.
                                Do not write all the conversation at once.
                                If there is an error, point it out.

                                Current Conversation:
                                {history}

                                Candidate: {input}
                                AI: """)

            st.session_state.jd_screen = ConversationChain(prompt=PROMPT, llm=llm,
                                                            memory=st.session_state.jd_memory)
        if 'jd_feedback' not in st.session_state:
            llm = ChatOpenAI(
                model_name="gpt-3.5-turbo",
                temperature=0.8, )
            st.session_state.jd_feedback = ConversationChain(
                prompt=PromptTemplate(input_variables=["history", "input"], template=templates.feedback_template),
                llm=llm,
                memory=st.session_state.jd_memory,
            )

    def answer_call_back():
        with get_openai_callback() as cb:
            # user input
            human_answer = st.session_state.answer
            # transcribe audio
            if voice:
                save_wav_file("temp/audio.wav", human_answer)
                try:
                    input = transcribe("temp/audio.wav")
                    # save human_answer to history
                except:
                    st.session_state.jd_history.append(Message("ai", "Sorry, I didn't get that."))
                    return "Please try again."
            else:
                input = human_answer

            st.session_state.jd_history.append(
                Message("human", input)
            )
            # OpenAI answer and save to history
            llm_answer = st.session_state.jd_screen.run(input)
            # speech synthesis and speak out
            audio_file_path = synthesize_speech(llm_answer, "openai")
            # create audio widget with autoplay
            audio_widget = Audio(audio_file_path, autoplay=True)
            # save audio data to history
            st.session_state.jd_history.append(
                Message("ai", llm_answer)
            )
            st.session_state.token_count += cb.total_tokens
            return audio_widget

    if jd:
        # initialize session states
        initialize_session_state_jd()
        #st.write(st.session_state.jd_guideline)
        credit_card_placeholder = st.empty()
        col1, col2 = st.columns(2)
        with col1:
            feedback = st.button("Get Interview Feedback")
        with col2:
            guideline = st.button("Show me interview guideline!")
        chat_placeholder = st.container()
        answer_placeholder = st.container()
        audio = None
        # if submit email adress, get interview feedback imediately
        if guideline:
            st.write(st.session_state.jd_guideline)
        if feedback:
            evaluation = st.session_state.jd_feedback.run("please give evalution regarding the interview")
            st.markdown(evaluation)
            st.download_button(label="Download Interview Feedback", data=evaluation, file_name="interview_feedback.txt")
            st.stop()
        else:
            with answer_placeholder:
                voice: bool = st.checkbox("I would like to speak with AI Interviewer")
                if voice:
                    answer = audio_recorder(pause_threshold = 2.5, sample_rate = 44100)
                    #st.warning("An UnboundLocalError will occur if the microphone fails to record.")
                else:
                    answer = st.chat_input("Your answer")
                if answer:
                    st.session_state['answer'] = answer
                    audio = answer_call_back()
            with chat_placeholder:
                for answer in st.session_state.jd_history:
                    if answer.origin == 'ai':
                        if auto_play and audio:
                            with st.chat_message("assistant"):
                                st.write(answer.message)
                                st.write(audio)
                        else:
                            with st.chat_message("assistant"):
                                st.write(answer.message)
                    else:
                        with st.chat_message("user"):
                            st.write(answer.message)

            credit_card_placeholder.caption(f"""
            Progress: {int(len(st.session_state.jd_history) / 30 * 100)}% completed.""")
    else:
        st.info("Please submit a job description to start the interview.")

########################################################################################
# Streamlit HomePage Setup

import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page
from PIL import Image

def HomePage():
    im = Image.open("images/icon.jpeg")
    st.set_page_config(page_title = "AI Interviewer", layout = "centered", page_icon=im)

    #role = st.selectbox("#### Role", ["Recruiter", "Candidate"])

    # if lan == "English":
    home_title = "AI Interviewer"
    home_introduction = "Welcome to AI Interviewer, empowering interviews with generative AI."
    with st.sidebar:
        st.markdown('AI Interviewer')
        st.markdown(""" 
        #### About Us:
        [Codebase](https://github.com/arnavailable/ai-interviewer)
        
        #### Support:
        [Arnav Garg](mailto:arnav.garg.2024@anderson.ucla.edu")
        
        [Alexandar Beltchev](mailto:alex.beltchev.2024@anderson.ucla.edu")
                    
        [Amber Li](mailto:amber.li.2024@anderson.ucla.edu")
                
        [Ray Xue](mailto:ray.xue.2024@anderson.ucla.edu")

        #### Powered by

        [Anthropic](https://www.anthropic.com/)

        [Langchain](https://www.langchain.com/)
        
        [Streamlit](https://streamlit.io/)

                    """)
    st.markdown(
        "<style>#MainMenu{visibility:hidden;}</style>",
        unsafe_allow_html=True
    )
    st.image(im, width=100)
    st.markdown(f"""# {home_title} <span style=color:#2E9BF5><font size=5>Beta</font></span>""",unsafe_allow_html=True)
    st.markdown("""\n""")
    #st.markdown("#### Greetings")
    st.markdown("Welcome to AI Interviewer! AI Interviewer is your personal interviewer powered by generative AI that conducts mock interviews."
                "You can upload your resume and enter job descriptions, and AI Interviewer will ask you customized questions. Additionally, you can configure your own Interviewer!")
    st.markdown("""\n""")
    # with st.expander("Updates"):
    #     st.write("""
    #     08/13/2023
    #     - Fix the error that occurs when the user input fails to be recorded. """)
    # with st.expander("What's coming next?"):
    #     st.write("""
    #     Improved voice interaction for a seamless experience. """)
    # st.markdown("""\n""")
    st.markdown("#### Get started!")
    st.markdown("Select one of the following screens to start your interview!")
    selected = option_menu(
            menu_title= None,
            options=["Recruiter", "Resume", "Technical", "Behavioral"],
            icons = ["cast", "cloud-upload", "cast"],
            default_index=0,
            orientation="horizontal",
        )
    if selected == 'Recruiter':
        st.info("""
            In this session, the AI Interviewer will assess your basic qualifications for the job such as your background and experience.
            - To start a new session, just refresh the page.
            - Choose your favorite interaction style (chat/voice)
            - Start by introducing yourself and enjoy！ """)
        # if st.button("Start Interview!"):
        #     # switch_page("Professional Screen")

    if selected == 'Resume':
        st.info("""
        Coming soon!""")
        # if st.button("Start Interview!"):
        #     switch_page("Resume Screen")

    if selected == 'Technical':
        st.info("""
        Coming soon!""")
        # if st.button("Start Interview!"):
        #     switch_page("Technical Screen")

    if selected == 'Behavioral':
        st.info("""
        Coming soon!""")
        # if st.button("Start Interview!"):
        #     switch_page("Behavioral Screen")
    # if selected == 'Customize!':
    #     st.info("""
    #         📚In this session, you can customize your own AI Interviewer and practice with it!
    #             - Configure AI Interviewer in different specialties.
    #             - Configure AI Interviewer in different personalities.
    #             - Different tones of voice.
                
    #             Coming at the end of July""")
    st.markdown("""\n""")

########################################################################################
# Streamlit Navigation

pg = st.navigation([
    st.Page(HomePage, title="Home Page", icon="🔥"),
    st.Page(ResumeScreenPage, title="Resume Screen", icon="📄"),
    st.Page(TechnicalScreenPage, title="Technical Screen", icon="🔧"),
    st.Page(BehavioralScreenPage, title="Behavioral Screen", icon="🧠")
])
pg.run()

########################################################################################
# Streamlit Main

# HomePage()

########################################################################################