"""
使用LazyLLM和Kimi模型的NBA数据分析应用
"""
import lazyllm
import os
import json
from nba_data_fetcher import fetch_nba_data, NBADataFetcher
from flask import Flask, render_template, jsonify


# 初始化Flask应用
flask_app = Flask(__name__, template_folder='templates', static_folder='static')


class NBAAnalysisAgent:
    """NBA数据分析智能体"""
    
    def __init__(self):
        # 获取Kimi API密钥
        self.kimi_api_key = os.environ.get('LAZYLLM_KIMI_API_KEY')
        if not self.kimi_api_key:
            print("警告: 未设置LAZYLLM_KIMI_API_KEY环境变量")
        
        # 初始化Kimi模型
        self.chat = lazyllm.OnlineChatModule(
            api_key=self.kimi_api_key,
            source='kimi',
            model='kimi-k2-0905-preview'
        )
        
        # 数据获取器
        self.data_fetcher = NBADataFetcher()
        
    def analyze_data(self, query: str = None) -> str:
        """
        使用Kimi模型分析NBA数据
        """
        # 获取最新数据
        nba_data = self.data_fetcher.get_all_data()
        
        # 构建提示词
        if not query:
            query = "请分析波特兰开拓者队本赛季的表现，特别关注中国球员杨瀚森的数据和表现。"
        
        prompt = f"""
你是一位专业的NBA数据分析师。以下是波特兰开拓者队和中国球员杨瀚森的最新数据：

{json.dumps(nba_data, ensure_ascii=False, indent=2)}

请根据以上数据{query}

请用专业、客观的语言进行分析，包括：
1. 球队整体表现
2. 杨瀚森的个人表现和进步空间
3. 最近比赛的亮点
4. 未来展望
"""
        
        try:
            # 调用Kimi模型
            response = self.chat(prompt)
            return response
        except Exception as e:
            return f"分析出错: {str(e)}\n\n原始数据:\n{json.dumps(nba_data, ensure_ascii=False, indent=2)}"
    
    def get_summary(self) -> dict:
        """获取数据摘要"""
        return self.data_fetcher.get_all_data()


# 创建全局agent实例
agent = NBAAnalysisAgent()


@flask_app.route('/')
def index():
    """主页"""
    return render_template('index.html')


@flask_app.route('/api/data')
def get_data():
    """API: 获取NBA数据"""
    data = agent.get_summary()
    return jsonify(data)


@flask_app.route('/api/analysis')
def get_analysis():
    """API: 获取AI分析"""
    try:
        analysis = agent.analyze_data()
        return jsonify({
            'success': True,
            'analysis': analysis
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


def main():
    """主函数"""
    print("="*60)
    print("🏀 NBA开拓者队数据分析系统")
    print("="*60)
    print("\n正在启动Web服务器...")
    print("\n访问 http://localhost:23456 查看数据可视化")
    print("\n按 Ctrl+C 停止服务\n")
    print("="*60)
    
    # 启动Flask应用
    flask_app.run(host='0.0.0.0', port=23456, debug=False)


if __name__ == "__main__":
    main()
