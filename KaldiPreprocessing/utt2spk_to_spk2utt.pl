if ( @ARGV > 1 ) {
    die "Usage: utt2spk_to_spk2utt.pl [ utt2spk ] > spk2utt";
}

while(<>){ 
    @A = split(" ", $_);
    @A == 2 || die "Invalid line in utt2spk file: $_";
    ($u,$s) = @A;
    if(!$seen_spk{$s}) {
        $seen_spk{$s} = 1;
        push @spklist, $s;
    }
    push (@{$spk_hash{$s}}, "$u");
}
foreach $s (@spklist) {
    $l = join(' ',@{$spk_hash{$s}});
    print "$s $l\n";
}