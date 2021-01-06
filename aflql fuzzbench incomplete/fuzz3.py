import shutil,os
import subprocess
import sys
import time

from fuzzers import utils


def prepare_build_environment():
    """Set environment variables used to build targets for AFL-based
    fuzzers."""
    cflags = ['-fsanitize-coverage=trace-pc-guard']
    utils.append_flags('CFLAGS', cflags)
    utils.append_flags('CXXFLAGS', cflags)

    os.environ['CC'] = 'clang'
    os.environ['CXX'] = 'clang++'
    os.environ['FUZZER_LIB'] = '/libAFL.a'
    
   
def build():
    """Build benchmark."""
    prepare_build_environment()
    utils.build_benchmark()
    shutil.copy('/afl/afl-fuzz', os.environ['OUT'])
    #shutil.copy('fuzzers/aflql/litool.ql',os.environ['OUT']+'/new/litool.ql')
    src = os.getenv('SRC')
    work = os.getenv('WORK')
    print('[post_build] Copying afl-fuzz to $OUT directory')
    
    
        #cur = os.getcwd()
    #with utils.restore_directory(src):
        #print('current dir is :')
        #print(cur)
    shutil.copytree(src,os.environ['OUT']+'/new')
    #os.chdir(os.environ['OUT'])
    #types.h
    shutil.copy('/afl/types.h', os.environ['OUT']+'/bbbbbaaaaa')
    os.system('ls -la')
    os.system('pwd')
    time.sleep(30)
    #os.system('unset WORKDIR')
    #os.system('unset SRC')
    #os.environ['SRC'] = '/out'
    #os.environ['OUT'] = '/out'
    shutil.copy('../fuzzers/aflql/litool.ql',os.environ['OUT']+'/new/litool.ql',follow_symlinks=False)
    #shutil.copy('fuzzers/aflql/litool.ql',os.environ['OUT']+'/new/litool.ql')
    print('Done!')

def prepare_fuzz_environment(input_corpus):
    """Prepare to fuzz with AFL or another AFL-based fuzzer."""
    # Tell AFL to not use its terminal UI so we get usable logs.
    os.environ['AFL_NO_UI'] = '1'
    # Skip AFL's CPU frequency check (fails on Docker).
    os.environ['AFL_SKIP_CPUFREQ'] = '1'
    # No need to bind affinity to one core, Docker enforces 1 core usage.
    os.environ['AFL_NO_AFFINITY'] = '1'
    # AFL will abort on startup if the core pattern sends notifications to
    # external programs. We don't care about this.
    os.environ['AFL_I_DONT_CARE_ABOUT_MISSING_CRASHES'] = '1'

    # AFL needs at least one non-empty seed to start.
    utils.create_seed_file_for_empty_corpus(input_corpus)


def run_afl_fuzz(input_corpus,
                 output_corpus,
                 target_binary,
                 additional_flags=None,
                 hide_output=False):
    """Run afl-fuzz."""
    # Spawn the afl fuzzing process.
    # FIXME: Currently AFL will exit if it encounters a crashing input in seed
    # corpus (usually timeouts). Add a way to skip/delete such inputs and
    # re-run AFL.
    print('[run_afl_fuzz] Running target with afl-fuzz')
    command = [
        './afl-fuzz',
        '-i',
        input_corpus,
        '-o',
        output_corpus,
        # Use deterministic mode as it does best when we don't have
        # seeds which is often the case.
        '-d',
        # Use no memory limit as ASAN doesn't play nicely with one.
        '-m',
        'none',
        '-t',
        '1000+',  # Use same default 1 sec timeout, but add '+' to skip hangs.
    ]
    if additional_flags:
        command.extend(additional_flags)
    dictionary_path = utils.get_dictionary_path(target_binary)
    if dictionary_path:
        command.extend(['-x', '/out/new/dict/'])
    command += [
        '--',
        target_binary,
        # Pass INT_MAX to afl the maximize the number of persistent loops it
        # performs.
        '2147483647'
    ]
    print('[run_afl_fuzz] Running command: ' + ' '.join(command))
    output_stream = subprocess.DEVNULL if hide_output else None
    subprocess.check_call(command, stdout=output_stream, stderr=output_stream)


def fuzz(input_corpus, output_corpus, target_binary):
    """Run afl-fuzz on target."""
    prepare_fuzz_environment(input_corpus)

    run_afl_fuzz(input_corpus, output_corpus, target_binary)
