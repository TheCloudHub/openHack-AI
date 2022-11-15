from azure.core.credentials import AzureKeyCredential

from azure.ai.language.questionanswering import QuestionAnsweringClient



#endpoint = "https://ohqa123.api.cognitive.microsoft.com/"



endpoint = "https://ohqa123.cognitiveservices.azure.com/"

credential = AzureKeyCredential("Ypur credential")

knowledge_base_project = "Challenge1"

deployment = "production"



def main():

    client = QuestionAnsweringClient(endpoint, credential)

    with client:

        question="How can I cancel my hotel reservation?"

        output = client.get_answers(

            question = question,

            project_name=knowledge_base_project,

            deployment_name=deployment

        )

    print("Q: {}".format(question))

    print("A: {}".format(output.answers[0].answer))



if __name__ == '__main__':

    main()