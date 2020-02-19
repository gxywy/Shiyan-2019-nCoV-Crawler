import datetime
from pyecharts.charts import Map
from pyecharts import options as opts
from pyecharts.globals import ThemeType
from crawler import get_data, get_article

today_url = get_article()
if today_url is not None:
    data = get_data(today_url)

    summary = "更新日期:" + str(datetime.date.today()) + ", 数据来源:十堰市政府官网\n累计确诊:" + data[0][1] + "例, 累计出院:" + data[1][1] + "例, 累计死亡:" + data[2][1] + "例"

    map = (
        Map(init_opts=opts.InitOpts(bg_color="#FFFAFA", theme=ThemeType.ROMANTIC, width=1000))
            .add("确诊人数", data, "十堰", is_map_symbol_show=False, )
            .set_global_opts(
            title_opts=opts.TitleOpts(title="十堰疫情确诊人数分布图 (By: Microyu)", subtitle=summary, pos_left="left"),
            visualmap_opts=opts.VisualMapOpts(
                is_piecewise=True,
                pieces=[
                    {"min": 201, "label": '>200人', "color": "#4F060d"},
                    {"min": 101, "max": 200, "label": '101-200人', "color": "#CB2A2F"},
                    {"min": 51, "max": 100, "label": '51-100人', "color": "#E45A4F"},
                    {"min": 10, "max": 50, "label": '10-50人', "color": "#F79D83"},
                    {"min": 1, "max": 9, "label": '1-9人', "color": "#FCEBCF"},
                ],
                range_text=['高', '低'],
            ),
        )
    )
    map.render(path="./index.html")