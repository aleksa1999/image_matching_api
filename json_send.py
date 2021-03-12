import requests
import base64
import json
import sys


def make_request_get_feature_img_filename(img_file_name):
    json_data = {
        "type": "get_feature_filename",
        "image": img_file_name
    }
    return json_data


def make_request_get_feature_img_base64(img_file):
    file_data = open(img_file, 'rb')
    json_data = {
        "type": "get_feature_base64",
        "image": base64.b64encode(file_data.read()).decode('UTF-8')
    }
    return json_data


def make_request_get_feature_img_link(img_file_name):
    json_data = {
        "type": "get_feature_link",
        "image": img_file_name
    }
    return json_data


def make_request_match_img_filename(img_file_name, acc=0.8):
    json_data = {
        "type": "match_filename",
        "accuracy": acc,
        "image": img_file_name
    }
    return json_data


def make_request_match_img_base64(img_file, acc=0.8):
    file_data = open(img_file, 'rb')
    json_data = {
        "type": "match_base64",
        "accuracy": acc,
        "image": base64.b64encode(file_data.read()).decode('UTF-8')
    }
    return json_data


def make_request_match_img_link(img_file_name, acc=0.8):
    json_data = {
        "type": "match_link",
        "accuracy": acc,
        "image": img_file_name
    }
    return json_data


def make_request_match_feature(img_feature, acc=0.8):
    json_data = {
        "type": "match_feature",
        "accuracy": acc,
        "image": img_feature
    }
    return json_data


def send_request(server, req_json):
    response = requests.post(url=server, json=req_json)
    print("Server responded with %s" % response.status_code)

    response_json = response.json()
    return response_json


if __name__ == '__main__':
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = '../1.png'
        # filename = 'https://asset.conrad.com/media10/isa/160267/c1/-/en/301550_BB_00_FB/image?x=400&y=400&ex=400&ey=400&align=center&format=jpg'

    url_server = 'http://localhost:3000/image_service/v1.0'
    # url_server = 'http://149.202.76.203:3000/image_service/v1.0'

    # json_request = make_request_get_feature_img_filename(filename)
    # json_request = make_request_get_feature_img_base64(filename)
    # json_request = make_request_get_feature_img_link(filename)
    # json_request = make_request_match_img_filename(filename)
    # json_request = make_request_match_img_base64(filename)
    # json_request = make_request_match_img_link(filename)

    feature = "{\"result\":{\"feature\":\"[0.13205051, 0.16701862, 0.18179958, 0.0, 0.32239312, 1.0030154, 0.34571248, 0.13847308, 0.5825874, 0.16078992, 0.5477977, 0.0, 0.07588226, 0.031915553, 0.21450527, 0.07523718, 0.01629244, 0.4110263, 0.11573847, 0.1665219, 0.46640778, 0.096331604, 0.1084046, 0.28225434, 0.1031414, 0.2489235, 0.27233902, 0.94435644, 0.3643219, 0.24288483, 0.06648627, 0.05254536, 0.9480384, 0.20956169, 0.17998917, 0.013419754, 0.25194937, 0.17142044, 0.0199171, 0.020491652, 0.0006034139, 0.50446236, 0.023670908, 0.3190788, 0.27823168, 0.108461246, 0.08160866, 0.103578076, 0.03291254, 0.030020911, 0.18287176, 0.16276106, 0.14734621, 0.007453632, 0.21029797, 0.11580102, 0.031082079, 0.5989603, 0.058893673, 0.027900914, 0.00879158, 0.054235876, 0.03500569, 0.33448538, 0.09360996, 0.29273143, 0.17557786, 0.09406451, 0.13116162, 0.01232541, 0.04838232, 0.6060795, 0.012450801, 0.48007193, 0.27510077, 0.0434277, 0.10801193, 0.42538813, 0.16022721, 0.029124558, 0.4428657, 0.05361127, 0.019542955, 0.47905582, 0.1668295, 0.4673169, 0.15710264, 1.4689182, 0.011435537, 0.15206374, 0.057912946, 0.11715155, 0.060055196, 0.16653447, 0.16991341, 0.04247384, 0.24101698, 0.63496494, 0.0890678, 0.54904014, 0.017721888, 0.19753364, 0.07874667, 0.21155897, 0.42620254, 0.38934344, 0.41791272, 0.13656513, 0.19800629, 0.041408412, 0.5526849, 0.3002865, 0.07073586, 0.16029648, 0.013490554, 0.22218102, 0.049855012, 0.45964628, 0.18275043, 0.0479765, 0.014043566, 0.005537375, 0.0016358679, 0.022708867, 0.09194116, 0.15601228, 0.037575155, 0.04132391, 0.27899978, 0.010332515, 0.04647076, 0.0370289, 0.15962178, 0.061140597, 0.029807147, 1.1104779, 0.029363833, 0.042407334, 0.020168917, 0.032794207, 0.027176414, 0.091584004, 0.21827108, 0.067432426, 0.019591521, 0.17186148, 0.04070398, 0.4037768, 0.14568414, 0.5978457, 0.20740385, 0.38853574, 0.24224503, 0.1741094, 1.1726182, 0.303969, 0.17718834, 0.06667674, 0.07546064, 0.16483624, 0.21676004, 0.010143253, 0.23189029, 0.046729967, 0.8697673, 0.124197796, 0.13143463, 0.20113641, 0.59666187, 0.122283034, 0.4475082, 0.11180416, 0.669544, 0.07544187, 0.2257664, 0.087824665, 0.10382702, 0.18218999, 0.03371122, 0.008241826, 0.12300588, 0.16531163, 0.06577815, 0.099349, 0.1879656, 0.021460231, 0.24385181, 0.48269224, 0.17694779, 0.13976103, 0.60412955, 0.34758675, 0.63614357, 0.061784368, 0.40317258, 0.011253383, 0.08856186, 0.034910917, 0.0066692107, 0.512674, 0.0, 0.031769827, 0.9044465, 0.3838042, 0.74070835, 0.18174425, 0.0019984986, 0.1988646, 0.44029477, 0.0057442915, 0.0033399828, 0.115438856, 0.02721138, 0.062020313, 0.14668651, 0.027544364, 0.19904557, 0.114976235, 0.10394909, 0.026389223, 0.56559795, 0.1308709, 0.19872768, 0.26341546, 0.021303806, 0.11940368, 0.10446907, 0.18841271, 0.07236535, 0.04352527, 0.56690687, 0.33656168, 0.21413524, 0.47147155, 0.3586999, 0.2454654, 1.6287446, 0.08045701, 0.07837215, 0.013832768, 0.011629237, 0.60767543, 0.01705864, 0.36146262, 0.18706426, 0.20773874, 0.11092578, 0.8389306, 0.135944, 0.26746884, 0.6151222, 0.11858993, 0.80685204, 0.5109491, 0.07523739, 0.70808756, 0.09700966, 0.50452614, 0.22788616, 0.33536544, 0.068111956, 0.40982422, 0.05424796, 0.34747306, 0.73476595, 0.4319657, 0.09198539, 0.019291978, 0.14146972, 0.31246102, 0.068538405, 0.048800934, 0.85629576, 0.005889067, 0.23188512, 0.0760591, 0.054488465, 0.0, 0.22549151, 0.37186185, 0.41669473, 0.010092215, 0.37426937, 0.20216851, 0.22722697, 0.20351832, 0.48697644, 0.002273962, 0.053465676, 0.04613918, 0.06226517, 0.11677457, 0.031886067, 0.10136854, 0.3758246, 0.007348956, 0.23085536, 0.36009738, 0.13358583, 0.15816854, 0.4200229, 0.42447016, 0.29751754, 0.041910887, 0.04612421, 0.016143778, 0.119810276, 0.0373809, 0.13976915, 0.012436915, 0.35468844, 0.70376694, 0.032779556, 0.080353886, 0.06065302, 0.9073638, 0.069261506, 1.001527, 0.8926228, 0.12119793, 0.0062325518, 0.038985018, 0.22526924, 0.0699737, 0.070063554, 0.35605264, 0.034730114, 0.019132696, 0.22325328, 0.24672012, 0.9205487, 0.00026986748, 0.10583766, 0.19251318, 0.0154503565, 0.0021433942, 0.26195255, 0.0004728341, 0.09405072, 0.03717775, 0.4387653, 0.05771852, 0.09081262, 0.07287465, 0.011725801, 0.156459, 0.33147594, 0.09147929, 0.1109489, 0.1795227, 0.09129129, 0.17470549, 0.073238194, 0.2935111, 0.22496273, 0.1516242, 0.00608388, 0.040220845, 0.2856179, 0.028025206, 0.45951244, 0.14051007, 0.09134383, 0.051934298, 0.001129807, 0.0144607965, 0.367603, 0.13308936, 0.07253857, 0.019472212, 0.06621713, 0.39058495, 0.031952117, 0.35167983, 0.004315415, 0.006212547, 0.45186454, 0.23445086, 0.7778083, 0.3891294, 0.023410719, 0.096357465, 0.34214616, 0.007410012, 0.11845485, 0.107436836, 0.018163057, 0.0082913805, 0.5464671, 0.08806669, 0.013161757, 0.055275097, 0.0, 0.019078963, 0.21451645, 0.22533946, 0.08011181, 0.3454875, 0.12371613, 0.026355617, 0.10024744, 0.008597236, 0.004285964, 0.2711729, 0.0016683955, 0.24585927, 0.78309315, 0.28743055, 0.03015201, 0.14969261, 0.07202399, 0.0028572963, 0.3141827, 0.03433461, 0.0, 0.15334938, 0.04057763, 0.064039186, 0.3249002, 0.13270818, 0.10374426, 0.02895919, 0.79342175, 0.0058018705, 0.3112976, 0.0006032337, 0.44576862, 0.6708469, 0.07221011, 0.47736886, 0.24287808, 0.114252575, 0.21769157, 0.12312467, 0.65428436, 0.264092, 0.15732743, 0.13597725, 0.10881542, 0.40821308, 0.22615652, 0.97945875, 0.07189441, 0.055401653, 0.13909063, 0.04079607, 0.008407446, 0.0005516554, 0.046215188, 0.6076714, 0.0, 0.07910677, 0.077966556, 0.45604506, 0.062745206, 0.08841206, 0.4436483, 0.037989527, 0.541188, 0.063085094, 0.0048614093, 0.27934295, 0.010251882, 0.044726696, 0.24273843, 0.24202232, 0.0285008, 0.03654254, 0.29255047, 0.5122428, 0.13994288, 0.23417309, 0.09334306, 0.21802045, 0.48425892, 0.23492628, 0.031703584, 0.18026224, 0.100965925, 0.050882306, 0.027024284, 0.022272142, 0.34078056, 0.026903132, 0.18619731, 0.17211393, 0.007020992, 0.027581105, 0.039906085, 0.560966, 0.15463188, 0.24068697, 0.43366313, 0.4157767, 0.0513611, 0.5704811, 0.026742656, 0.14013273, 0.51056004, 0.29354122, 0.03259748, 0.22812782, 0.6771594, 0.30268267, 0.22593105, 0.03318878, 0.020301694, 0.038283005, 0.09692671, 0.019246604, 0.18611953, 0.0, 0.112816654, 0.048637114, 0.030691849, 0.8277017, 0.39322948, 0.10767852, 0.061606526, 0.32279852, 0.45855993, 0.20680128, 0.19186229, 0.21091625, 0.21299747, 0.046607535, 0.0863574, 0.3656801, 0.23727468, 0.06174049, 0.29765603, 0.34910682, 0.8270959, 1.3216629, 0.17061038, 0.10602947, 0.092679076, 0.18352278, 0.2780535, 0.0738092, 0.30483353, 0.05926859, 0.29219157, 0.043732367, 0.03238162, 0.14747055, 0.05495894, 0.100858845, 0.10904463, 0.03095515, 0.45974156, 0.23475331, 0.575067, 0.0, 0.3109362, 0.057160355, 0.19948454, 0.073171794, 0.006815607, 0.13790667, 0.030722948, 0.18453653, 1.5657912, 0.16224404, 0.492976, 0.17924629, 0.0073316814, 0.16984792, 0.26904503, 0.31109634, 0.036107335, 0.1342264, 0.08112868, 0.0028773216, 0.09084731, 0.80465746, 0.019670852, 0.0, 0.007112044, 0.013712192, 0.5464533, 0.0037341863, 0.1221461, 0.08816936, 0.06747146, 0.5558321, 0.2974071, 0.029369637, 0.23515874, 0.019943437, 0.18198323, 0.07091613, 0.0014807244, 0.23559089, 0.040677633, 0.044525806, 0.09609246, 0.07023598, 0.12832022, 0.6584133, 0.07486174, 0.3199089, 0.042718217, 0.066682965, 0.028075647, 0.42769665, 0.09699461, 0.48308682, 0.027606696, 0.27404088, 0.8975409, 0.12501343, 0.042708922, 0.38183248, 0.6437447, 0.06560319, 1.2646083, 0.0035613962, 0.0127912825, 0.08953902, 0.83492136, 0.44618106, 0.024270436, 0.1883943, 0.010384612, 0.0002975755, 0.34532592, 0.16710955, 0.16948971, 0.19544166, 0.21711281, 0.3554772, 0.092153914, 0.21509172, 0.5315117, 0.09105654, 0.019779077, 0.18769963, 0.3833032, 0.6460447, 0.026729798, 0.106933236, 0.00058164634, 0.78488415, 0.21193665, 0.36365122, 0.15935719, 0.24493451, 0.015140217, 0.11708532, 0.044057705, 0.008847194, 0.1437967, 0.29760903, 0.253336, 0.2758102, 0.08050954, 0.10904132, 0.8228305, 0.0014945199, 0.02212216, 0.30827343, 0.09914684, 0.017541116, 0.550881, 0.1706745, 0.09754778, 0.04357887, 0.18584335, 0.003913033, 0.3492701, 0.017680554, 0.18515395, 1.0028071, 0.009888547, 0.2156812, 0.115764044, 1.0023062, 0.14880213, 0.08605166, 0.06507082, 0.37426308, 0.20974283, 0.29821944, 0.549939, 0.15970683, 0.35679698, 0.0032640824, 0.10406909, 0.0006358158, 0.0055292547, 0.19369304, 0.0590271, 0.45324084, 0.026078422, 0.06398003, 0.34496942, 0.057610292, 0.052167468, 0.21851486, 0.07171648, 0.025404425, 0.33938786, 0.16804042, 0.29317737, 0.13479686, 0.018177105, 0.15883659, 0.6793558, 0.009873874, 0.42008507, 0.16733223, 0.5243903, 0.33602288, 0.58276004, 0.0016680956, 0.06251128, 0.20352517, 0.27553675, 0.323666, 0.007061245, 0.32503557, 0.012740268, 0.22688815, 0.05565069, 0.4162936, 1.0188506, 0.10892563, 0.1711803, 0.18473832, 0.020042546, 0.2375025, 0.09037635, 0.0155240875, 0.6950563, 0.05040489, 0.5389531, 0.07729159, 0.21750745, 0.19040349, 0.0149121275, 0.300812, 0.10106759, 0.67635405, 0.047277637, 0.15982556, 0.01880736, 0.0010908658, 0.07543168, 0.16889171, 0.123464316, 0.2223608, 0.9453822, 0.6507553, 0.71480656, 0.3591061, 0.08472064, 0.10074466, 0.014778946, 0.7543075, 0.027518023, 0.0045966185, 0.45718253, 0.24009536, 0.50424105, 0.23962122, 0.10575103, 0.060151838, 0.10323437, 0.057823338, 0.04753887, 0.07698179, 0.09135087, 0.09068398, 0.046419688, 0.27919212, 0.006020487, 0.017542608, 0.4853038, 0.2531926, 0.3093178, 0.041849, 0.33192873, 0.2881516, 0.2691242, 0.20062006, 0.0048256386, 0.34998724, 0.0075936164, 0.59789765, 0.053166647, 0.10357286, 0.034804683, 0.13834508, 0.1561387, 0.06299779, 0.114928015, 0.7728272, 0.118349485, 0.36155877, 0.22709848, 0.10859141, 0.28084356, 0.2671115, 0.24320573, 0.07901069, 0.1728529, 0.112213835, 0.29071763, 0.382686, 0.14025857, 0.042219404, 0.23931013, 0.20174633, 0.049087983, 0.7924298, 0.0, 0.35094523, 0.17192222, 0.021317143, 0.15057196, 0.6770776, 0.26025084, 0.25149435, 0.001077143, 0.07582533, 0.46322143, 0.04467539, 0.3210361, 0.14779171, 0.55136657, 0.22994336, 0.0, 0.66491145, 0.013232343, 0.12543859, 0.16233169, 0.058762293, 0.063415065, 0.49585477, 0.0544493, 0.23118281, 0.05439192, 0.32437173, 0.017322108, 1.0618029, 0.03497353, 0.07252368, 0.28100953, 0.1827251, 0.005840407, 0.09739731, 0.03696595, 0.06663928, 0.118268736, 1.8386753, 0.51316047, 0.15017127, 1.0779173, 0.0480384, 0.32829282, 0.13807447, 0.027452564, 0.26590768, 0.3417578, 0.12937705, 0.3195985, 0.2854178, 0.0235551, 0.7458778, 0.15807611, 0.0045259837, 0.7205292, 0.001382773, 0.43961245, 0.1028739, 0.6628213, 0.1752665, 0.12721778, 0.028799068, 0.41512766, 0.011642855, 0.26024732, 0.13964602, 0.09398606, 0.0055549387, 0.25495973, 0.49469838, 0.027966514, 0.74709815, 0.13025117, 0.0019003353, 0.03520396, 0.7206453, 0.13185458, 0.06448853, 0.027958803, 0.39054853, 0.024678344, 0.010551532, 0.03922086, 0.3154477, 0.09044772, 0.41761997, 0.17185444, 0.18586084, 0.050523426, 0.13128118, 0.19373989, 0.09306757, 0.01627718, 0.028276052, 0.3861151, 0.014761822, 1.0667381, 0.047985084, 0.15249087, 0.07942462, 0.35074848, 0.7184358, 0.08532906, 0.40811276, 0.14341506, 0.26210657, 0.029625082, 0.06469271, 0.0, 0.5386016, 0.27342314, 0.09337941, 0.37500677, 0.02509396, 0.0, 0.0, 0.23711492, 0.2181473, 0.026687952, 0.315419, 0.051711023, 0.0, 0.02566287, 0.11148301, 0.42871916, 0.0023388867, 0.01520492, 0.1239434, 0.063358076, 0.06912998, 0.059058636, 0.5813472, 0.10594133, 0.36495307, 0.021374987, 0.281567, 0.5957695, 0.07075764, 0.27577406, 0.024667485, 1.1015531, 0.029678855, 0.03503146, 0.026603965, 0.2886529, 0.02517717, 0.045175232, 0.22918797, 0.054678906, 0.13358246, 0.41891706, 0.10046447, 0.12597379, 0.15172274, 0.03480843, 0.07217222, 0.0007817866, 0.55511916, 0.49046057, 0.04726573, 0.0, 0.37390348, 0.42974627, 0.16206874, 0.03862701, 0.32350543, 1.0978916, 0.06192694, 0.23084481, 0.15019427, 0.0, 0.006546881, 0.77394176, 0.428908, 0.24699517, 1.1875203, 0.30101275, 0.48945135, 0.017172653, 0.1766447, 0.44188243, 0.48096058, 0.095483385, 0.09032741, 0.14100239, 0.0067119272, 1.1907935, 0.30974543, 0.04190223, 0.27854687, 0.043688223, 0.0, 0.64179796, 0.20185733, 0.006901796, 0.044785462, 0.01612146, 0.25638267, 0.12560794, 0.14859773, 0.094649695, 0.43639392, 0.1022765, 0.027499575, 0.14461465, 0.016025797, 0.17159483, 0.6972379, 0.21544836, 0.11401631, 0.049433175, 0.15798798, 0.10619139, 0.4009753, 0.6180833, 0.6393695, 0.062148355, 0.0670488, 0.0030549814, 0.75608355, 0.018200738, 0.027598308, 0.28229022, 0.0, 0.28213245, 0.052325755, 0.020023406, 0.47274882, 0.06972104, 0.084995784, 0.19015184, 0.3911715, 0.080631144, 0.138076, 0.0012343461, 0.60813886, 0.16058557, 0.08024527, 0.00020872708, 0.013239445, 0.20772173, 0.18081377, 0.1675489, 0.0034178784, 0.005578639, 0.05727018, 0.03503554, 1.0034044, 0.10380765, 0.5194111, 0.092890956, 0.29540837, 0.017227456, 0.4461257, 0.494527, 0.40659827, 0.097277895, 0.045948535, 0.007016182, 0.117371865, 0.07327664, 0.11688195, 0.37299097, 0.13167778, 0.3403737, 0.82121205, 0.00050348695, 0.15987387, 0.21150327, 0.0015867506, 0.20127307, 0.11412998, 0.3278285, 0.19176224, 0.08901569, 0.37873688, 0.3783353, 0.2372316, 0.16937076, 0.4386586, 0.35026732, 0.69666594, 0.14060602, 0.5235129, 0.46854818, 0.24138747, 0.59049845, 0.54646206, 0.82171774, 0.41263393, 0.36062357, 0.20282437, 0.22838725, 0.14129235, 0.27449065, 0.07753799, 0.7270722, 0.14084168, 0.22911489, 0.23912944, 0.77219707, 0.32358268, 0.07080146, 0.14535403, 0.55208886, 0.26899824, 0.954031, 0.10248231, 0.3632973, 0.15736075, 0.21249354, 0.19626316, 0.6618109, 0.23659925, 0.37833315, 0.2749194, 0.5706952, 0.072214514, 0.06491483, 0.05831152, 0.56748056, 0.23092675, 0.31821132, 0.11953265, 0.49062952, 0.15883628, 0.63729835, 0.19574694, 0.47565654, 0.19086449, 0.31517306, 0.53154755, 0.17676842, 0.6048514, 0.1642691, 0.16416778, 0.07251787, 0.33711237, 1.1420655, 0.70953625, 0.39784852, 0.13865645, 0.33410898, 0.5409986, 0.5061415, 0.54994565, 0.096119605, 0.1823784, 0.14816146, 0.18845677, 0.7605979, 0.21201193, 0.015516529, 0.23300911, 0.41799474, 0.090619154, 0.12759268, 0.28155598, 0.37679073, 0.40029794, 0.2496535, 0.23969977, 0.12939401, 0.18721353, 0.18135387, 0.39042008, 0.19656287, 0.94682944, 0.2360957, 0.49690098, 0.22685786, 0.18556197, 0.11138171, 0.2868964, 0.10580011, 0.2867228, 0.026947312, 0.44909817, 0.12998228, 0.46328712, 0.10872744, 1.0588031, 0.55504185, 0.045248754, 0.056342643, 0.53080136, 0.73313093, 0.12643467, 0.060882125, 0.34088132, 0.80095357, 0.3031855, 0.20782697, 0.59492904, 0.16659598, 0.029629834, 0.6737625, 0.46590194, 0.027352232, 0.74416417, 0.19088696, 0.28022537, 0.0627073, 0.10272932, 0.25547493, 0.33644634, 0.04135732, 0.20234096, 0.28395218, 0.10334317, 0.6218182, 0.47707236, 0.23153025, 1.0555413, 0.5566614, 0.16300689, 0.43749818, 0.50221735, 0.30454576, 0.41569942, 0.014938655, 0.22038525, 0.15908721, 0.12723711, 0.14197366, 0.50092477, 0.42207024, 0.15975878, 0.48528323, 0.23892893, 0.35692322, 0.5390313, 0.26675662, 0.07047763, 0.36392397, 0.90641075, 0.3635095, 0.08575046, 0.89783317, 0.4959777, 0.1984913, 0.25842053, 0.453352, 0.13470368, 0.55983365, 0.036954787, 0.1354882, 0.28809226, 0.71734816, 0.30973768, 0.03520136, 0.28385997, 0.3252657, 0.5996067, 0.30843073, 0.026727937, 0.9912278, 0.43407056, 0.39689076, 0.4343695, 0.22447294, 0.08006067, 0.13569875, 0.30357632, 0.67413443, 0.38116804, 0.16962682, 0.47451296, 0.2568995, 0.23837236, 0.0061040763, 0.22960691, 0.14185691, 0.03766052, 0.044884007, 0.5053985, 0.384028, 0.18180767, 0.21970409, 0.1934223, 0.055485666, 0.596957, 0.081346944, 0.34911352, 0.15629846, 0.49338216, 0.90905905, 0.25140774, 0.46539626, 0.24943481, 0.11325843, 0.06679208, 1.0634228, 0.18619482, 0.38651362, 0.10360825, 0.17427397, 0.24893077, 0.20978585, 0.30468982, 0.13343748, 0.3091684, 0.26321122, 0.5428795, 0.57414967, 0.069917984, 0.73093224, 0.19750139, 0.06282251, 0.4383108, 0.5141584, 0.67731494, 0.152455, 0.1794316, 0.23024158, 0.34840518, 0.36408848, 0.031423938, 0.28739098, 0.123745665, 0.14082485, 0.3866648, 0.042900212, 0.15160191, 0.14725433, 0.09985072, 0.39985824, 0.54841727, 0.469794, 0.02428088, 0.6498975, 0.19127795, 0.27469394, 0.47745913, 0.35956535, 0.071459144, 0.107036844, 0.15301852, 0.40449452, 0.68518764, 0.1983568, 0.42286348, 0.25377992, 0.08571186, 0.15989007, 0.24414685, 0.18658823, 0.23913635, 0.48718008, 0.33684617, 0.43215033, 0.4583937, 0.19222225, 0.2523975, 0.4350801, 0.1339074, 0.47983894, 0.28165162, 0.16924207, 0.2485622, 0.19085906, 0.5146241, 0.068435796, 0.4790129, 0.1402795, 0.22872469, 0.35517454, 0.16735013, 0.05819282, 0.030304957, 0.3396647, 0.34866464, 0.72424823, 0.72394234, 0.21847661, 0.430403, 0.21090229, 0.33772868, 0.6784425, 0.17336425, 0.26929152, 0.1416014, 0.2598907, 0.24225688, 0.29416186, 0.26102257, 0.34011254, 0.3849362, 0.32209724, 0.16891709, 0.68029463, 0.115433134, 0.28733245, 0.17476706, 0.21323225, 0.032721944, 0.09101606, 0.29253712, 0.15666862, 0.661771, 0.5675202, 0.22316381, 0.46630216, 0.116165236, 0.26214388, 0.26223582, 0.41578472, 0.13759555, 0.21898296, 0.1496175, 0.1714192, 0.37641072, 0.3131823, 0.27480096, 0.32952917, 0.011322055, 0.2441415, 0.3417781, 0.71218616, 0.33922386, 0.22640236, 0.55287087, 0.24665284, 0.04010699, 0.53089505, 0.33279017, 0.054823577, 0.3773744, 0.16388275, 0.47230583, 0.049817845, 0.14246489, 0.25089744, 0.51372397, 0.30337358, 0.9051645, 0.24556841, 0.17927094, 0.63780034, 0.093187205, 0.23805533, 0.2805087, 0.0089749135, 0.00027178926, 0.7181578, 0.33891144, 0.20365573, 0.93776566, 0.229891, 0.3121301, 0.397729, 0.3702489, 0.23478939, 0.1712637, 0.11219166, 0.11266675, 0.034699857, 0.15423027, 0.28882504, 0.24501212, 0.2524216, 0.19568375, 0.21009547, 0.27926838, 0.25372094, 0.2681458, 0.33842856, 0.1396458, 0.15760797, 0.13484311, 0.4668847, 0.72217536, 0.45670944, 0.48753086, 0.68643916, 0.10833614, 0.64752626, 0.54507476, 0.014891799, 0.094141476, 0.3893343, 0.38542038, 0.52616006, 0.84050965, 0.30373392, 0.28261188, 0.70394975, 0.27232775, 0.2595949, 0.048559256, 0.17095786, 0.20647736, 0.0013583596, 0.053006224, 0.14012441, 0.3748911, 0.1789938, 0.7392771, 0.24579723, 0.08154151, 0.10475329, 0.46272328, 0.4798519, 0.060695812, 0.8907021, 0.1830013, 0.36038077, 0.31862274, 0.7277314, 0.42178372, 0.33571124, 0.034124307, 0.551815, 0.1729061, 0.28807908, 0.45271412, 0.61204433, 0.56940776, 0.114750296, 0.4391362, 0.5609154, 0.5436977, 0.49916285, 0.48337877, 0.16838595, 0.14622687, 0.6387542, 0.07136592, 0.17669147, 0.7562996, 0.74433243, 0.07942991, 0.9368616, 0.19731772, 0.20443042, 0.39608905, 0.48703814, 0.70501286, 0.18905973, 0.12577434, 0.18022554, 0.061462153, 0.59103936, 0.517234, 0.46900776, 0.32606658, 0.6673705, 0.12309955, 0.4626999, 0.09506723, 0.7164295, 0.10787149, 0.34364063, 0.53750855, 0.33861643, 0.2643044, 0.29011476, 0.36558446, 0.46659264, 0.36844996, 0.5319238, 0.48338082, 0.5192417, 0.32341722, 0.3696147, 0.6360472, 0.17767219, 0.81983644, 0.09259451, 0.6659297, 0.4875151, 0.78191257, 0.04293776, 0.117785, 0.23832159, 0.101362444, 0.6716599, 0.2560047, 0.4990471, 0.010579303, 0.23105507, 0.62141424, 0.045809705, 0.35064432, 0.59229016, 0.37814972, 0.15848257, 0.10394283, 0.5667794, 0.29260734, 0.39285582, 0.07393615, 0.26909393, 0.018740403, 0.69056106, 0.25350764, 0.30722666, 0.2981283, 0.2967834, 0.5279809, 0.4850705, 0.009849457, 0.23250179, 0.333974, 0.3110174, 0.035102274, 0.5010235, 0.080763124, 0.6028665, 0.02753961, 0.5900862, 0.32233706, 0.32669723, 0.21225648, 0.52377164, 0.4389481, 0.34776232, 0.8587235, 0.4223515, 0.9900228, 0.24474086, 0.23348995, 0.17482427, 0.15718201, 0.29243046, 0.14475356, 0.93124396, 0.041578244, 0.12531719, 0.24952479, 0.039482348, 0.34112585, 0.20881009, 0.2724339, 0.4206954, 0.24126624, 0.26807025, 0.12262785, 0.47656637, 0.08657866, 0.7721049, 0.111858435, 0.48301545, 0.29241136, 0.0047632596, 0.21196999, 0.68066657, 0.40912372, 1.361299, 0.5482052, 0.75498235, 0.19870791, 0.21661997, 0.29323792, 0.46340656, 0.40502083, 0.45835647, 0.73552155, 0.45893183, 0.085940674, 0.078587696, 0.28706565, 0.2165008, 0.12563477, 0.15913837, 0.37212798, 0.54798084, 0.40431052, 0.6979556, 0.3869747, 0.43722427, 0.51871043, 0.022087673, 0.54456323, 0.89959013, 0.22120377, 0.37626502, 0.120941855, 0.56678677, 0.28554454, 0.5725189, 0.10018335, 0.24731857, 0.8898402, 0.39564562, 0.06390178, 0.5030752, 0.14070629, 0.32719415, 0.23248439, 0.42658576, 0.2719148, 0.17657706, 0.21994501, 0.30470154, 0.47960007, 0.6712924, 0.14328647, 0.20651977, 0.5717697, 0.49672017, 0.5136236, 0.396245, 0.48308334, 0.11075108, 0.16936189, 0.47685066, 0.1398738, 0.124742344, 0.19285586, 0.4338083, 0.62540233, 0.2890056, 0.35818663, 0.2830612, 0.46012124, 0.5575523, 0.49993697, 0.06655662, 0.3851444, 0.49831825, 0.36623123, 0.12373482, 0.11163292, 0.3506969, 0.15151249, 0.31517208, 0.9812512, 0.11494006, 0.6577308, 0.32650644, 0.22587255, 0.8770261, 0.62891054, 0.099995464, 0.19485357, 0.06769303, 0.4634246, 0.7051294, 0.48475316, 0.32780862, 0.25885153, 0.3440683, 0.82520026, 0.22241436, 0.52541363, 0.1666595, 0.5767836, 0.26663914, 0.3520278, 0.22884536, 0.08069901, 0.18100971, 0.061889067, 0.27738652, 0.93501896, 0.16927132, 0.102903694, 0.27036196, 0.21977264, 0.4741248, 0.31015217, 0.13293672, 0.2670119, 0.49631757, 0.15749149, 0.42289945, 0.2192468, 0.09628533, 0.05906282, 0.471638, 0.11604047, 0.088743575, 0.031581547, 0.23331791, 0.5247752, 0.95775163, 0.07261596, 0.282864, 0.10066469, 0.2165612, 0.014484823, 0.35734534, 0.14432628, 0.15080181, 0.790046, 0.43940797, 0.1519754, 0.26482326, 0.38664982, 0.19524139, 0.36801124, 0.73250586, 0.008294752, 0.117572844, 0.12803183, 0.21840392, 0.48362157, 1.0096492, 0.48799178, 0.016679121, 0.1981816, 0.24303268, 0.63092375, 0.09129734, 0.4226897, 0.28826064, 0.56496906, 0.17830423, 0.52284455, 0.4448684, 1.0087553, 0.20671234, 0.3251673, 0.3287651, 0.12763847, 0.6922436, 0.022827161, 0.18132083, 0.48322314, 0.14322144, 0.26628396, 0.45265368, 0.0139158815, 0.4250603, 0.3884823, 0.14232165, 0.25057098, 0.93398434, 0.28747112, 0.29106537, 0.571428, 0.25562078, 0.44706333, 0.08026812, 0.30400026, 0.25665706, 0.09099948, 0.6589364, 0.01951359, 0.0, 0.55561286, 0.10137784, 0.0, 0.5846278, 0.579988, 0.72326916, 0.96857345, 0.81331104, 0.28762975, 0.6626797, 0.35718173, 0.24277778, 0.028792562, 0.08500508, 0.5303285, 0.9540881, 0.12210801, 0.14654179, 0.3189679, 0.060131446, 0.28500903, 0.120558865, 0.005538006, 0.0034868324, 0.007857645, 0.18401594, 0.2409149, 0.65751135, 0.053426664, 0.49200404, 0.0015634751, 0.42834273, 0.0030886517, 0.24904367, 0.23633249, 0.41434112, 0.3152492, 0.0, 0.54101866, 0.29211193, 0.42088687, 0.24898821, 0.27277327, 0.032711346, 0.13618189, 0.12772335, 0.0021071471, 0.06762975, 0.20002948, 0.031231329, 0.432104, 0.0, 0.0865366, 0.016802501, 0.73976314, 0.41355157, 7.0412774e-05, 0.1465759, 0.32042292, 0.08602697, 0.3908745, 0.6880337, 0.2534793, 0.054837834, 0.061703674, 0.018088408, 0.49945858, 0.24962547, 0.040359337, 0.061403304, 0.1679349, 0.0, 0.0, 0.6230739, 0.17317095, 0.08278514, 0.35888636, 0.0033663367, 0.5711979, 0.055412717, 0.0, 0.0, 0.07718343, 0.1892378, 0.016526168, 0.011192553, 0.33156806, 0.7550105, 0.018763276, 1.1092702, 0.08507736, 0.7555694, 0.39677796, 0.5896886, 0.008323263, 0.07064711, 0.35825104, 0.051862888, 0.18447606, 0.10445783, 0.92912924, 0.05376491, 0.020397268, 0.60361814, 0.4980014, 0.21121894, 0.27336097, 0.5341115, 0.8398002, 0.030809883, 0.27678367, 0.035627495, 0.06625061, 0.51687604, 0.59742826, 0.12466184, 0.0026152646, 0.2797019, 0.43113032, 0.1901232, 0.10776752, 0.32072142, 0.020447338, 0.029639553, 0.29683527, 0.26722568, 0.27046636, 0.0084062265, 0.50497806, 0.68246937, 0.41706526, 0.008517534, 0.61533964, 0.0004956203, 0.025895976, 0.09114813, 0.13947704, 0.08546446, 0.0041099475, 0.23635599, 0.0063934745, 0.18209037, 0.14627947, 0.047609907, 0.2197031, 0.67526823, 0.012360664, 0.3071258, 0.05046939, 0.30602184, 0.57135814, 0.40261686, 0.40362346, 0.018015645, 0.34316805, 0.025868844, 0.078698635, 0.027013024, 0.53272647, 0.11776479, 0.38153175, 0.08648792, 0.0, 0.8930213, 0.044201132, 0.24517682, 0.36812007, 0.0014356562, 0.24959368, 0.06714541, 0.43555412, 0.3564743, 0.14155486, 0.3870043, 0.48046, 0.15376827, 0.04426339, 0.113138124, 0.042317454, 0.18054724, 0.14315988, 0.018519193, 0.60986817, 0.44064257, 0.0, 0.0, 0.50270003, 0.21081826, 0.0060263807]\"}}\n"
    json_request = make_request_match_feature(feature)

    ret_response = send_request(url_server, json_request)
    # print(json.dumps(ret_response, indent=4))

    print(len(ret_response["result"]["match"]))
    for i in ret_response["result"]["match"]:
        print(ret_response["result"]["match"][i]['accuracy'])
