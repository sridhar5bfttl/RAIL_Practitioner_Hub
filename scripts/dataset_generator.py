import pandas as pd
import numpy as np
import os

def generate_telemetry_data():
    np.random.seed(42)
    
    # 1. Generate Historical Data (Stable Operations)
    n_historical = 1000
    historical_data = pd.DataFrame({
        'timestamp': pd.date_range(start='2026-01-01', periods=n_historical, freq='H'),
        'temperature': np.random.normal(70, 5, n_historical),
        'pressure': np.random.normal(2500, 100, n_historical),
        'vibration': np.random.normal(0.5, 0.1, n_historical),
        'status': 'normal'
    })
    
    # 2. Generate Real-time Data (The "Drift" and "Anomaly")
    n_realtime = 200
    realtime_data = pd.DataFrame({
        'timestamp': pd.date_range(start='2026-02-12', periods=n_realtime, freq='H'),
        'temperature': np.random.normal(72, 6, n_realtime), # Slight increase
        'pressure': np.random.normal(2550, 150, n_realtime), # More volatility
        'vibration': np.random.normal(0.5, 0.1, n_realtime),
        'status': 'normal'
    })
    
    # Inject Sensor Drift (Gradual temperature increase)
    realtime_data.loc[100:, 'temperature'] += np.linspace(0, 15, 100)
    
    # Inject Novel Anomaly (Vibration spike unknown to historical patterns)
    realtime_data.loc[150:, 'vibration'] += np.random.normal(2.0, 0.5, 50)
    realtime_data.loc[150:, 'status'] = 'fault_novel'
    
    # Create directory if not exists
    data_dir = '/Volumes/superfast/LinkedIn/RAIL/RAIL_Practitioner_Hub/data'
    os.makedirs(data_dir, exist_ok=True)
    
    # Save files
    historical_path = os.path.join(data_dir, 'historical_rig_data.csv')
    realtime_path = os.path.join(data_dir, 'realtime_rig_telemetry.csv')
    
    historical_data.to_csv(historical_path, index=False)
    realtime_data.to_csv(realtime_path, index=False)
    
    print(f"Data generated successfully in {data_dir}")
    print(f"Historical: {historical_path}")
    print(f"Real-time: {realtime_path}")

if __name__ == "__main__":
    generate_telemetry_data()
