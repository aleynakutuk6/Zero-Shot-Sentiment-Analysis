import json


def write_sentiment_intent_results(results, save_path):
    final_dict = []
    for sent_res, intent_res in results:
        assert sent_res["sequence"] == intent_res["sequence"]

        sent_dict = {}
        assert len(sent_res["labels"]) == len(sent_res["scores"])
        for i in range(len(sent_res["labels"])):
            sent_dict[sent_res["labels"][i]] = sent_res["scores"][i]

        intent_dict = {}
        assert len(intent_res["labels"]) == len(intent_res["scores"])
        for i in range(len(intent_res["labels"])):
            intent_dict[intent_res["labels"][i]] = intent_res["scores"][i]

        final_dict.append(
            {
                "sentence": sent_res["sequence"],
                "sentiment_results": sent_dict,
                "intention_results": intent_dict,
            }
        )

    with open(save_path, "w") as f:
        json.dump(final_dict, f)
