from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

def calculate_yields(investment, dpr, wpr, tvl, weekly_rewards):
    # Calculate yields
    daily_yield = investment * (dpr / 100)
    weekly_yield = investment * (wpr / 100)
    monthly_yield = investment * ((1 + (dpr / 100)) ** 30 - 1)
    yearly_yield = investment * ((1 + (dpr / 100)) ** 365 - 1)
    proportion = weekly_rewards * (investment / tvl)
    
    return {
        'daily_yield': round(daily_yield, 2),
        'weekly_yield': round(weekly_yield, 2),
        'monthly_yield': round(monthly_yield, 2),
        'yearly_yield': round(yearly_yield, 2),
        'proportion': round(proportion, 2)
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    try:
        results = calculate_yields(
            float(data['investment']),
            float(data['dpr']),
            float(data['wpr']),
            float(data['tvl']),
            float(data['weekly_rewards'])
        )
        return jsonify({'success': True, 'results': results})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True) 